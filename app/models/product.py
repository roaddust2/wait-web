from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """Categories of products"""

    name = models.CharField(_('Category'), max_length=255)
    image = models.ImageField(_('Image'), upload_to='static/images/categories/')
    image_alt = models.CharField(_('ImageAlt'), max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(models.Model):
    """Product model"""

    name = models.CharField(_('Denomination'), max_length=255)
    description = models.TextField(_('Description'), max_length=600)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name=_('Category'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('CareatedAt'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductImage(models.Model):
    """Image model connected with product"""

    image = models.ImageField(_('Image'), upload_to='static/images/products/')
    image_alt = models.CharField(_('ImageAlt'), max_length=255, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'))
    default = models.BooleanField(default=False, verbose_name=_('Default'))

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
