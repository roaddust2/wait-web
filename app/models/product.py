from django.db import models
from utils.text import FormFields


vname = FormFields()


class Category(models.Model):
    """Categories of products"""

    name = models.CharField(vname.category_name, max_length=255)
    image = models.ImageField('Image', upload_to='static/images/categories/')
    image_alt = models.CharField(
        'Image alternative text',
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    """Product model"""

    name = models.CharField(vname.product_name, max_length=255)
    description = models.TextField(vname.product_description, max_length=600)
    price = models.DecimalField(
        vname.product_price,
        max_digits=10,
        decimal_places=2,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name=vname.product_category,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    """Image model connected with product"""

    image = models.ImageField('Image', upload_to='static/images/products/')
    image_alt = models.CharField(
        'Image alternative text',
        max_length=200,
        null=True,
        blank=True,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Product',
    )
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.image.url
