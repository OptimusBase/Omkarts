"""Model."""
from decimal import Decimal
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail
from accounts.models import UserAddress
from carts.models import Cart
from products.models import Variation
# Create your models here.

REASON = (
    ('Changed My Mind', 'Changed My Mind'),
    ('Discovered the same product at a lower price ', 'Discovered the same product at a lower price '),
    ("I don't need it any more", "I don't need it any more"),
    ('Product is taking too long to be delivered', 'Product is taking too long to be delivered'),
    ('Received damaged product', 'Received damaged product'),)

CANCEL_ORDER = (('Yes', 'Yes'), ('No', 'No'))

CANCEL_ORDER_STATUS = (('Refund Not Initiated', 'Not Initiated'), ('Refund Initiated', 'Refund Initiated'), ('Amount Refunded', 'Refunded'))

# STATUS_CHOICES = (
#     ("Created", "Created"),
#     ("Placed", "Placed"),
#     ("Started", "Started"),
#     ("Abandoned", "Abandoned"),
#     ("Finished", "Finished"),)

PAYMENT_CHOICES = (
    ("Not Paid", "Not Paid"),
    ("Cash on delivery", "Cash on delivery"),
    ("Paid", "Paid"),)

try:
    tax_rate = settings.DEFAULT_TAX_RATE
except Exception, e:
    print str(e)
    raise NotImplementedError(str(e))


class Order(models.Model):
    """Order Model."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True)

    order_id = models.CharField(
        max_length=128,
        default='ABC',
        unique=True)

    cart = models.ForeignKey(
        Cart,
        null=True,
        blank=True)

    # status = models.CharField(
    #     max_length=128,
    #     choices=STATUS_CHOICES,
    #     default="Created")

    payment = models.CharField(
        max_length=128,
        choices=PAYMENT_CHOICES,
        default="Not Paid")

    razor_payment_id = models.CharField(
        max_length=225,
        blank=True,
        null=True,
        default="")

    shipping_address = models.ForeignKey(
        UserAddress,
        related_name='shipping_address',
        default=1)

    sub_total = models.DecimalField(
        max_digits=100,
        decimal_places=2,
        default=10.99)

    tax_total = models.DecimalField(
        max_digits=100,
        decimal_places=2,
        default=0.00)

    final_total = models.DecimalField(
        max_digits=100,
        decimal_places=2,
        default=10.99)

    timestamp = models.DateTimeField(
        auto_now_add=True,
        auto_now=False)

    updated = models.DateTimeField(
        auto_now_add=False,
        auto_now=True)

    def __unicode__(self):
        """Unicode."""
        return self.order_id

    def get_final_amount(self):
        """Final amount calculation."""
        instance = Order.objects.get(id=self.id)
        two_places = Decimal(10) ** -2
        tax_rate_dec = Decimal("%s" % (tax_rate))
        sub_total_dec = Decimal(self.sub_total)
        tax_total_dec = Decimal(tax_rate_dec * sub_total_dec).quantize(two_places)
        instance.tax_total = tax_total_dec
        instance.final_total = sub_total_dec + tax_total_dec
        instance.save()
        return instance.final_total


class OrderCancellationRequest(models.Model):
    """OrderCancellationRequest."""

    order = models.OneToOneField(
        Order)

    variation = models.ForeignKey(
        Variation,
        default="",
        blank=False,
        null=False)

    reason = models.CharField(
        max_length=255,
        choices=REASON,
        default="",
        blank=False,
        null=False,
        verbose_name="Reason For Cancellation.")

    other_reason = models.TextField(
        default="",
        verbose_name="Anything else you would like to tell us?")

    cancel_order = models.CharField(
        max_length=255,
        choices=CANCEL_ORDER,
        default="",
        blank=True,
        null=True,
        verbose_name='Cancel Order ?',
        help_text='Select Yes if you want to cancel the order else select No')

    # user_notification = models.TextField(
    #     # max_length=255,
    #     default="",
    #     blank=True,
    #     null=True,
    #     # choices=CANCEL_ORDER,
    #     verbose_name='Message for customer.',
    #     help_text='Please give the reason if the order cannot be cancelled')

    user_notification = models.CharField(
        max_length=128,
        choices=CANCEL_ORDER,
        blank=True,
        null=True,
        default="")

    resend_notification = models.BooleanField(
        default=False)

    cancel_status = models.CharField(
        max_length=255,
        default='Refund Not Initiated',
        blank=False,
        null=False,
        choices=CANCEL_ORDER_STATUS,
        verbose_name='Order Status')

    active = models.BooleanField(
        default=True)

    def __unicode__(self):
        """Unicode."""
        return str(self.order.order_id)


def user_notification_cancel(sender, instance, created, *args, **kwargs):
    import ipdb; ipdb.set_trace()
    if instance.resend_notification is True:
        if instance.cancel_order == 'Yes':
            for x in instance.order.cartitem_set.all():
                if x.variation == instance.variation:
                    status = x.status
            subject = "Your order for %s %s %s %s has been %s" % (instance.variation.product.title, instance.variation.storage, instance.variation.color, instance.variation.screen_size, status)
            message = "Some Body text."
            try:
                for user_email in instance.order.user.emailaddress_set.all():
                    if user_email.primary is True:
                        email_to = user_email.email
            except:
                email_to = None

            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [email_to], fail_silently=False)
                instance.resend_notification = False
            except:
                print ("Send email failed at Post signal for cartitem status.")

            instance.user_notification = 'Yes'
            instance.resend_notification = False
            instance.save()
            # Initiate Refund
            # instance.cancel_status == 'Refund Initiated'
            # instance.save()

        if instance.cancel_order == 'No':
            subject = "Your order for %s %s %s %s cannot be cancelled" % (instance.variation.product.title, instance.variation.storage, instance.variation.color, instance.variation.screen_size)
            message = " Hi %s, \n We are sorry to inform you that your request for Product cancellation cannot be processed as it does not pass our return policy. \n Check our return Policy for more information.\n Warm Regards \n Customer Care" % (instance.order.user)

            try:
                for user_email in instance.order.user.emailaddress_set.all():
                    if user_email.primary is True:
                        email_to = user_email.email
            except:
                email_to = None

            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [email_to], fail_silently=False)
                instance.resend_notification = False
                instance.user_notification = 'No'
            except:
                print ("Send email failed at Post signal for cartitem status.")
                instance.resend_notification = False

            instance.save()

            # Initiate Refund
            # instance.cancel_status == 'Refund Initiated'
            # instance.save()
    else:
        if not instance.cancel_order == instance.user_notification:
            if instance.cancel_order == 'Yes':
                for x in instance.order.cartitem_set.all():
                    if x.variation == instance.variation:
                        x.status = 'Cancelled'
                        x.save()

                        instance.user_notification = 'Yes'
                        instance.resend_notification = False
                        instance.save()
                        # Initiate Refund
                        # instance.cancel_status == 'Refund Initiated'
                        # instance.save()
            if instance.cancel_order == 'No':
                subject = "Your order for %s %s %s %s cannot be cancelled" % (instance.variation.product.title, instance.variation.storage, instance.variation.color, instance.variation.screen_size)
                message = " Hi %s, \n We are sorry to inform you that your request for Product cancellation cannot be processed as it does not pass our return policy. \n Check our return Policy for more information.\n Warm Regards \n Customer Care" % (instance.order.user)

                try:
                    for user_email in instance.order.user.emailaddress_set.all():
                        if user_email.primary is True:
                            email_to = user_email.email
                except:
                    email_to = None

                try:
                    send_mail(subject, message, settings.EMAIL_HOST_USER, [email_to], fail_silently=False)
                    instance.resend_notification = False
                    instance.user_notification = 'No'
                except:
                    print ("Send email failed at Post signal for cartitem status.")
                    instance.resend_notification = False

                instance.save()

                # Initiate Refund
                # instance.cancel_status == 'Refund Initiated'
                # instance.save()

post_save.connect(user_notification_cancel, sender=OrderCancellationRequest)
