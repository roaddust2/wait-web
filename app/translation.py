from modeltranslation.translator import register, TranslationOptions
from .models.product import Category, Product


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)
