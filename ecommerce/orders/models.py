"""Model."""
from decimal import Decimal
from django.conf import settings
from django.db import models

from accounts.models import UserAddress
from carts.models import Cart
# Create your models here.

STATUS_CHOICES = (
    ("Created", "Created"),
    ("Placed", "Placed"),
    ("Started", "Started"),
    ("Abandoned", "Abandoned"),
    ("Finished", "Finished"),)

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

    status = models.CharField(
        max_length=128,
        choices=STATUS_CHOICES,
        default="Created")

    payment = models.CharField(
        max_length=128,
        choices=PAYMENT_CHOICES,
        default="Not Paid")

    shipping_address = models.ForeignKey(
        UserAddress,
        related_name='shipping_address',
        default=1)

    billing_address = models.ForeignKey(
        UserAddress,
        related_name='billing_address',
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
        tax_rate_dec = Decimal("%s" %(tax_rate))
        sub_total_dec = Decimal(self.sub_total)
        tax_total_dec = Decimal(tax_rate_dec * sub_total_dec).quantize(two_places)
        instance.tax_total = tax_total_dec
        instance.final_total = sub_total_dec + tax_total_dec
        instance.save()
        return instance.final_total
