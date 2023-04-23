from modeltranslation.translator import register, TranslationOptions
from django.contrib.flatpages.models import FlatPage
from .models.home import CarouselItem
from .models.product import Category, Product, ProductFeature


@register(FlatPage)
class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(CarouselItem)
class CarouselTranslationOptions(TranslationOptions):
    fields = ('label', 'placeholder',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


@register(ProductFeature)
class ProductFeatureTranslationOptions(TranslationOptions):
    fields = ('feature',)
