from uuid import uuid4
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from app.models.abstract import AbstractImage


def category_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    path = "images/categories/{0}.{1}".format(uuid4().hex, ext)
    return path


class Category(AbstractImage):
    """Categories of products"""

    category_slug = models.SlugField(_('Category'), unique=True)
    name = models.CharField(_('Category'), max_length=255)
    description = models.TextField(_('Description'), max_length=600)
    image = models.ImageField(
        _('Image'),
        width_field='image_width',
        height_field='image_height',
        upload_to=category_directory_path
    )
    image_width = models.IntegerField(blank=True, null=True)
    image_height = models.IntegerField(blank=True, null=True)
    image_webp = models.ImageField(upload_to=category_directory_path, null=True, blank=True)
    image_alt = models.CharField(_('ImageAlt'), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return the url of an instance."""
        return reverse(
            'category',
            args=[self.category_slug],
        )


class Product(models.Model):
    """Product model"""

    product_slug = models.SlugField(_('Denomination'), unique=True)
    name = models.CharField(_('Denomination'), max_length=255)
    description = models.TextField(_('Description'), max_length=600)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name=_('Category'))
    sold = models.BooleanField(default=False, verbose_name=_('Sold'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('CareatedAt'))

    def get_all_features(self):
        """Returns the product's related ауфегкуы from ProductFeature model"""
        images = self.productfeature_set.all()
        return images

    def get_all_images(self):
        """Returns the product's related images from ProductImage model, defaults first"""
        images = self.productimage_set.all().order_by('-default')
        return images

    def get_default_image(self):
        """Returns the product's first availible default image, or first in a set"""
        try:
            default_image = self.productimage_set.get(default=True)
            return default_image
        except ProductImage.DoesNotExist:
            return self.productimage_set.first()

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return the url of an instance."""
        return reverse(
            'product',
            args=[
                self.category.category_slug,
                self.product_slug],
        )


class ProductFeature(models.Model):
    """Features model (size, weight, color, etc.) connected with product"""

    feature = models.CharField(_('Feature'), max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'))

    def __str__(self):
        return self.feature

    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')
        ordering = ['id']


def productimage_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    path = "images/products/{0}.{1}".format(uuid4().hex, ext)
    return path


class ProductImage(AbstractImage):
    """Image model connected with product"""

    image = models.ImageField(
        _('Image'),
        width_field='image_width',
        height_field='image_height',
        upload_to=productimage_directory_path
    )
    image_width = models.IntegerField(blank=True, null=True)
    image_height = models.IntegerField(blank=True, null=True)
    image_webp = models.ImageField(upload_to=productimage_directory_path, null=True, blank=True)
    image_alt = models.CharField(_('ImageAlt'), max_length=255, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'))
    default = models.BooleanField(default=False, verbose_name=_('Default'))

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
