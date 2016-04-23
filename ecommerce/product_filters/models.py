"""Models."""
from django.db import models
from products.models import SubCategoryParent
from product_description.models import PdpSpecificationType
# from smart_selects.db_fields import ChainedForeignKey
# Create your models here.


class ProductQuerySet(models.query.QuerySet):
    """ProductQuerySet."""

    def active(self):
        """Active."""
        return self.filter(active=True)


class ProductFilterManager(models.Manager):
    """ProductFilterManager."""

    def active(self):
        """Active."""
        return super(ProductFilterManager, self).filter(active=True)


class ProductFilter(models.Model):
    """Class to create product filters."""

    sub_cat_parent = models.OneToOneField(
        SubCategoryParent,
        default="")

    active = models.BooleanField(
        default=True)

    objects = ProductFilterManager()

    # filter_field = ChainedForeignKey(
    #     PdpSpecification,
    #     chained_field="sub_cat_child",
    #     chained_model_field="sub_cat_child",
    #     show_all=False,
    #     auto_choose=True)

    def __unicode__(self):
        """Unicode Class."""
        return str(self.sub_cat_parent)


class ProductFilterAttributes(models.Model):
    """ProductFilterAttributes."""

    product_filter = models.ForeignKey(
        ProductFilter)

    filter_field = models.ForeignKey(
        PdpSpecificationType,
        default="")

    active = models.BooleanField(
        default=True)

    objects = ProductFilterManager()

    def __unicode__(self):
        """Unicode Class."""
        return str(self.filter_field)    
