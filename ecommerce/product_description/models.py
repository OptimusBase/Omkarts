"""T."""
from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from products.models import Variation

ICON_TYPE = (('Google', 'Google'), ('Font-Awesome', 'Font-Awesome'))


class PdpSpecificationType(models.Model):
    """PdpSpecifications Model."""

    # variation = models.ForeignKey(
    #     Variation,
    #     null=True,
    #     blank=True)

    specification_type = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Specification type',
        help_text='Enter Product Specification type. Example "Brand" ')

    # active = models.BooleanField(
    #     default=True)

    def __unicode__(self):
        """Unicode Class."""
        return str(self.specification_type)


class PdpSpecification(models.Model):
    """PdpSpecifications Model."""

    variation = models.ForeignKey(
        Variation,
        null=True,
        blank=True)

    specification_type = models.ForeignKey(
        PdpSpecificationType,
        default="")

    specification_value = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Specification value',
        help_text='Enter Product Specification value. Example "Apple" ')

    active = models.BooleanField(
        default=True)

    def __unicode__(self):
        """Unicode Class."""
        return str(self.variation)


class PdpDescription(models.Model):
    """PdpDescription Model."""

    variation = models.ForeignKey(
        Variation,
        null=True,
        blank=True)

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Description',
        help_text='Enter Product Description.')

    active = models.BooleanField(
        default=True)

    def __unicode__(self):
        """Unicode Class."""
        return str(self.variation)


class PdpKeyFeature(models.Model):
    """PdpKeyFeature Model."""

    variation = models.ForeignKey(
        Variation,
        null=True,
        blank=True)

    icon_type = models.CharField(
        max_length=225,
        choices=ICON_TYPE,
        default='Google',
        verbose_name='Icon type',
        help_text='Enter Key Feature Icon Type. Select the option of which you want icons of.')

    icon_class = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        default="",
        verbose_name='Icon Class',
        help_text='Enter Key Feature Icon Class. This is required only if you want Font-Awesome icons')

    title = models.TextField(
        blank=True,
        null=True,
        verbose_name='Key Feature Text',
        help_text='Enter Key Feature Text.')

    active = models.BooleanField(
        default=True)

    def __unicode__(self):
        """Unicode Class."""
        return str(self.variation)


class PdpPhysicalFeature(models.Model):
    """PdpPhysicalFeature Model."""

    variation = models.ForeignKey(
        Variation,
        null=True,
        blank=True)

    key_feature_image = models.ImageField(
        upload_to='product_description/images/physical_feature',
        blank=True,
        null=True,
        verbose_name='Physical Feature Image',
        help_text='Enter Product Physical Feature Image.')

    active = models.BooleanField(
        default=True)

    def __unicode__(self):
        """Unicode Class."""
        return str(self.variation)


class PdpFeatured(models.Model):
    """PdpFeatured Model."""

    variation = models.ForeignKey(
        Variation,
        null=True,
        blank=True)

    featured_image = models.ImageField(
        upload_to='product_description/images/featured',
        blank=True,
        null=True,
        verbose_name='Featured Image',
        help_text='Enter Product Featured Image.')

    header = models.TextField(
        blank=True,
        null=True,
        verbose_name='Featured header',
        help_text='Enter Product Featured Header.')

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Featured description',
        help_text='Enter Product Featured description.')

    order = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Featured Order',
        help_text='The product featured item will be shown in this order.')

    active = models.BooleanField(
        default=True)

    def __unicode__(self):
        """Unicode Class."""
        return str(self.variation)
