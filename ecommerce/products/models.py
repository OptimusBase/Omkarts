"""Models Class."""
from django.core.urlresolvers import reverse
from django.db import models
import datetime
# from django.db.models.signals import post_save
# Create your models here.


class Category(models.Model):
    """docstring for ClassName."""

    category_name = models.CharField(
        max_length=120,
        null=True,
        blank=True)

    description = models.TextField(
        null=True,
        blank=True)

    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True)

    featured = models.BooleanField(
        default=False)

    timestamp = models.DateTimeField(
        auto_now_add=True,
        auto_now=False)

    updated = models.DateTimeField(
        auto_now_add=False,
        auto_now=True)

    active = models.BooleanField(
        default=True)

    def __unicode__(self):
        """Unicode class."""
        return str(self.category_name)


class SubCategoryParent(models.Model):
    """docstring for ClassName."""

    category = models.ForeignKey(
        Category,
        null=True,
        blank=True)

    sub_cat_parent_name = models.CharField(
        max_length=120,
        null=True,
        blank=True)

    description = models.TextField(
        null=True,
        blank=True)

    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True)

    featured = models.BooleanField(
        default=False)

    timestamp = models.DateTimeField(
        auto_now_add=True,
        auto_now=False)

    updated = models.DateTimeField(
        auto_now_add=False,
        auto_now=True)

    active = models.BooleanField(
        default=True)

    def __unicode__(self):
        """Unicode class."""
        return str(self.sub_cat_parent_name)


class SubCategoryChild(models.Model):
    """docstring for ClassName."""

    sub_category_parent = models.ForeignKey(
        SubCategoryParent,
        null=True,
        blank=True)

    sub_cat_child_name = models.CharField(
        max_length=120,
        null=True,
        blank=True)

    description = models.TextField(
        null=True,
        blank=True)

    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True)

    featured = models.BooleanField(
        default=False)

    timestamp = models.DateTimeField(
        auto_now_add=True,
        auto_now=False)

    updated = models.DateTimeField(
        auto_now_add=False,
        auto_now=True)

    active = models.BooleanField(
        default=True)

    def __unicode__(self):
        """Unicode class."""
        return str(self.sub_cat_child_name)


class Brand(models.Model):
    """docstring for ClassName."""

    brand_name = models.CharField(
        max_length=120,
        null=True,
        blank=True)

    description = models.TextField(
        null=True,
        blank=True)

    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True)

    timestamp = models.DateTimeField(
        auto_now_add=True,
        auto_now=False)

    updated = models.DateTimeField(
        auto_now_add=False,
        auto_now=True)

    featured = models.BooleanField(
        default=False)

    active = models.BooleanField(
        default=True)

    def __unicode__(self):
        """Unicode class."""
        return str(self.brand_name)


class BrandConfiguration(models.Model):
    """Brand Config."""

    brand = models.ForeignKey(
        Brand,
        null=True,
        blank=True)

    sub_category_parent = models.ForeignKey(
        SubCategoryParent,
        null=True,
        blank=True)

    featured = models.BooleanField(
        default=False)

    order = models.IntegerField(
        blank=True,
        null=True)

    def __unicode__(self):
        """Unicode class."""
        return str(self.brand.brand_name)


class Product(models.Model):
    """Product class."""

    category = models.ForeignKey(
        Category,
        default="",
        null=False,
        blank=False)

    sub_category_parent = models.ForeignKey(
        SubCategoryParent,
        default="",
        null=False,
        blank=False)

    sub_category_child = models.ForeignKey(
        SubCategoryChild,
        default="",
        null=False,
        blank=False)

    brand = models.ForeignKey(
        Brand,
        default="",
        null=False,
        blank=False)

    title = models.CharField(
        max_length=120,
        null=False,
        blank=False)  # blank field means required field, null is for empty value.

    image = models.ImageField(
        upload_to='products/images',
        default="",
        blank=False,
        null=False)

    # description = models.TextField(
    #     null=True,
    #     blank=True)

    # price = models.DecimalField(
    #     decimal_places=2,
    #     max_digits=100,
    #     default=0.0)

    # sale_price = models.DecimalField(
    #     decimal_places=2,
    #     max_digits=100,
    #     null=True,
    #     blank=True)

    slug = models.SlugField(
        unique=True)

    timestamp = models.DateTimeField(
        auto_now_add=True,
        auto_now=False)

    updated = models.DateTimeField(
        auto_now_add=False,
        auto_now=True)

    active = models.BooleanField(
        default=True)

    # update_defaults = models.BooleanField(
    #     default=False)

    def __unicode__(self):
        """Unicode class."""
        return self.title

    class Meta:
        unique_together = ('title', 'slug')

    def get_price(self):
        """Some method."""
        return self.price

    # def get_absolute_url(self):
    #     return reverse("single_product", kwargs={"slug": self.slug})


class VariationManager(models.Manager):
    def all(self):
        return super(VariationManager, self).filter(active=True)

    # def storage(self):
    #     return self.all().filter(category='storage')

    # def colors(self):
    #     return self.all().filter(category='color')

    # def screen_size(self):
    #     return self.all().filter(category='screen_size')


# VAR_CATEGORIES_COLOR = (
#     ('storage', 'storage'),
#     ('color', 'color'),
#     ('screen_size', 'screen_size'))

# VAR_CATEGORIES_STORAGE = (
#     ('storage', 'storage'),
#     ('color', 'color'),
#     ('screen_size', 'screen_size'))

# VAR_CATEGORIES_SCREEN_SIZE = (
#     ('storage', 'storage'),
#     ('color', 'color'),
#     ('screen_size', 'screen_size'))


class Variation(models.Model):
    product = models.ForeignKey(
        Product)

    color = models.CharField(
        max_length=120,
        # choices=VAR_CATEGORIES,
        null=True,
        blank=True)

    storage = models.CharField(
        max_length=120,
        # choices=VAR_CATEGORIES,
        null=True,
        blank=True)

    screen_size = models.CharField(
        max_length=120,
        # choices=VAR_CATEGORIES,
        null=True,
        blank=True)

    quantity = models.IntegerField(
        null=True,
        blank=True)

    price = models.DecimalField(
        decimal_places=2,
        max_digits=100,
        null=True,
        blank=True)

    timestamp = models.DateTimeField(
        auto_now_add=True,
        auto_now=False)

    updated = models.DateTimeField(
        auto_now_add=False,
        auto_now=True)

    active = models.BooleanField(
        default=True)

    objects = VariationManager()

    def __unicode__(self):
        return "%s, %s, %s" % (self.storage, self.color, self.screen_size)


class ProductImage(models.Model):
    """Product Image Class."""

    variation = models.ForeignKey(
        Variation,
        null=True,
        blank=True)

    image = models.ImageField(
        upload_to='Variation/images')

    # featured = models.BooleanField(
    #     default=False)

    thumbnail = models.BooleanField(
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
        """Unicode Class."""
        return str(self.variation)

# def product_defaults(sender, instance, created, *args, **kwargs):
#     import ipdb; ipdb.set_trace()
#     if instance.update_defaults:
#         categories = instance.category.all()
#         print categories
#         for cat in categories:
#             print cat.id
#             if cat.id == 1: #for t-shirts
#                 small_size = Variation.objects.get_or_create(product=instance, 
#                                             category='size', 
#                                             title='Small')
#                 medium_size = Variation.objects.get_or_create(product=instance, 
#                                             category='size', 
#                                             title='Medium')
#                 large_size = Variation.objects.get_or_create(product=instance, 
#                                             category='size', 
#                                             title='Large')
#         instance.update_defaults = False
#         instance.save()
#     #print args, kwargs

# post_save.connect(product_defaults, sender=Product)
