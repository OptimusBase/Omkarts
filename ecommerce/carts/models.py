from django.db import models
from products.models import Product, Variation
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings

STATUS_CHOICES = (
    ("Created", "Created"),
    ("Placed", "Placed"),
    ("Confirmed", "Confirmed"),
    ("Cancelled", "Cancelled"),
    ("Shipped", "Shipped"),
    ("Delivered", "Delivered"),)


class Cart(models.Model):
    total = models.DecimalField(
        max_digits=1000,
        decimal_places=2,
        default=0.00)

    timestamp = models.DateTimeField(
        auto_now_add=True,
        auto_now=False)

    updated = models.DateTimeField(
        auto_now_add=False,
        auto_now=True)

    active = models.BooleanField(
        default=True)

    def __unicode__(self):
        return "Cart id %s" % (self.id)


from orders.models import Order


class CartItem(models.Model):

    cart = models.ForeignKey(
        Cart,
        null=True,
        blank=True)

    product = models.ForeignKey(
        Product)

    variation = models.ForeignKey(
        Variation,
        null=True,
        blank=True)

    order = models.ForeignKey(
        Order,
        null=True,
        blank=True)

    quantity = models.IntegerField(
        default=1)

    line_total = models.DecimalField(
        max_digits=100,
        decimal_places=2,
        default=0,
        verbose_name='Total')

    notes = models.TextField(
        null=True,
        blank=True)

    status = models.CharField(
        max_length=128,
        choices=STATUS_CHOICES,
        default="Created")

    user_notification = models.CharField(
        max_length=128,
        choices=STATUS_CHOICES,
        default="Created")

    resend_notification = models.BooleanField(
        default=False)

    active = models.BooleanField(
        default=True)

    timestamp = models.DateTimeField(
        auto_now_add=True,
        auto_now=False)

    updated = models.DateTimeField(
        auto_now_add=False,
        auto_now=True)

    def __unicode__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.title


def user_notification(sender, instance, created, *args, **kwargs):
    user_notification_sent = False
    if not instance.status == instance.user_notification:
        subject = "Your order for %s %s %s %s has been %s" % (instance.product.title, instance.variation.storage, instance.variation.color, instance.variation.screen_size, instance.status)
        message = "Some Body text."

        try:
            for user_email in instance.order.user.emailaddress_set.all():
                if user_email.primary is True:
                    email_to = user_email.email
        except:
            email_to = None

        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email_to], fail_silently=False)
            instance.user_notification = instance.status
            user_notification_sent = True
        except:
            print ("Send email failed at Post signal for cartitem status.")
            user_notification_sent = False

        instance.save()

    if user_notification_sent is False and instance.resend_notification is True:
        subject = "Your order for %s %s %s %s has been %s" % (instance.product.title, instance.variation.storage, instance.variation.color, instance.variation.screen_size, instance.status)
        message = "Some Body text."

        try:
            for user_email in instance.order.user.emailaddress_set.all():
                if user_email.primary is True:
                    email_to = user_email.email
        except:
            email_to = None

        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email_to], fail_silently=False)
            user_notification_sent = True
            instance.resend_notification = False
        except:
            print ("Send email failed at Post signal for cartitem status.")
            user_notification_sent = False
            instance.resend_notification = False
        instance.save()

post_save.connect(user_notification, sender=CartItem)
