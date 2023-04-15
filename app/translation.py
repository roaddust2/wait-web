from modeltranslation.translator import register, TranslationOptions
from django.contrib.flatpages.models import FlatPage
from .models.product import Category, Product


@register(FlatPage)
class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
