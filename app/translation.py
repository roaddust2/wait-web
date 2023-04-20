from modeltranslation.translator import register, TranslationOptions
from django.contrib.flatpages.models import FlatPage
from .models.home import CarouselItem
from .models.product import Category, Product


@register(FlatPage)
class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(CarouselItem)
class CarouselTranslationOptions(TranslationOptions):
    fields = ('label', 'placeholder',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('int_name',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('int_name', 'description',)
