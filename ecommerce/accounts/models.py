from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

from localflavor.in_.in_states import STATE_CHOICES
from products.models import Product, Variation
NEW_STATE = STATE_CHOICES

GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'))
COUNTRY = (('India', 'India'),)


class UserInformation(models.Model):
    """docstring for UserInformation."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    name = models.CharField(
        max_length=120,
        null=True,
        blank=True)

    gender = models.CharField(
        max_length=8,
        choices=GENDER_CHOICES)

    country = models.CharField(
        max_length=8,
        choices=COUNTRY)

    birthdate = models.DateField(
        null=True,
        blank=True)

    timestamp = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        null=True,
        blank=True)

    updated = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        null=True,
        blank=True)

    def __unicode__(self):
        """Unicode Class."""
        return str(self.user)


class UserDefaultAddress(models.Model):
    """UserDefaultAddress."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    shipping = models.ForeignKey("UserAddress", null=True,\
                     blank=True, related_name="user_address_shipping_default")
    billing = models.ForeignKey("UserAddress", null=True,\
                    blank=True, related_name="user_address_billing_default")

    def __unicode__(self):
        """Unicode."""
        return str(self.user.username)


class UserAddressManager(models.Manager):
    """UserAddressManager."""

    def get_billing_addresses(self, user):
        """get_billing_addresses."""
        return super(UserAddressManager, self).filter(billing=True).filter(user=user)


class UserAddress(models.Model):
    """UserAddress."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=120, null=True, blank=True)
    address = models.CharField(max_length=120)
    address2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120, choices=NEW_STATE, null=True, blank=True, default='')
    country = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=25)
    phone = models.CharField(max_length=120, default='')
    shipping = models.BooleanField(default=True)
    billing = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        """Unicode."""
        return self.get_address()

    def get_address(self):
        """Get Address."""
        return "%s, %s, %s, %s, %s" %(self.address, self.city, self.state, self.country, self.zipcode)

    objects = UserAddressManager()

    class Meta:
        ordering = ['-updated', '-timestamp']


class UserStripe(models.Model):
    """UserStripe."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL)

    stripe_id = models.CharField(
        max_length=128,
        null=True,
        blank=True)

    def __unicode__(self):
        """Unicode."""
        return str(self.stripe_id)


class EmailConfirmed(models.Model):
    """EmailConfirmed."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL)

    activation_key = models.CharField(
        max_length=200)

    confirmed = models.BooleanField(default=False)

    def __unicode__(self):
        """Unicode."""
        return str(self.confirmed)

    def activate_user_email(self):
        """Activat user email."""
        activation_url = "%s%s" % (settings.SITE_URL, reverse("activation_view", args=[self.activation_key]))
        context = {
            "activation_key": self.activation_key,
            "activation_url": activation_url,
            "user": self.user.username,
        }
        message = render_to_string("accounts/activation_message.txt", context)
        subject = "Activate your email"
        self.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)

    def email_user(self, subject, message, from_email=None, *kwargs):
        """Email User."""
        send_mail(subject, message, from_email, [self.user.email], kwargs)


class EmailMarketingSignUp(models.Model):
    """Email Marketing SignUp."""

    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    # confirmed = models.BooleanField(default=False)

    def __unicode__(self):
        """Unicode."""
        return str(self.email)


class WishList(models.Model):
    """Wish List."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    product = models.ForeignKey(
        Product,
        null=True,
        blank=True)

    variation = models.ForeignKey(
        Variation,
        null=True,
        blank=True)

    active = models.BooleanField(
        default=True)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        """Unicode."""
        return str(self.user)


class RecentViews(models.Model):
    """Wish List."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True)

    variation = models.ForeignKey(
        Variation,
        null=True,
        blank=True)

    timestamp = models.DateTimeField(
        auto_now_add=True,
        auto_now=False)

    updated = models.DateTimeField(
        auto_now_add=False,
        auto_now=True)

    def __unicode__(self):
        """Unicode."""
        return str(self.user)
