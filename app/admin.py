from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models.user import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from .models.home import CarouselItem
from .models.product import Category, Product, ProductFeature, ProductImage


# Customized User

admin.site.register(CustomUser, UserAdmin)


# Internalized flatpages

admin.site.unregister(FlatPage)


@admin.register(FlatPage)
class CustomFlatPageAdmin(TranslationAdmin, FlatPageAdmin):
    model = FlatPage


# App's models register

@admin.register(CarouselItem)
class CarouselAdmin(TranslationAdmin):
    list_display = ('label', 'placeholder', 'link', 'priority')
    search_fields = ['label', 'placehilder']
    model = CarouselItem
    exclude = ['image_webp']


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    model = Category
    prepopulated_fields = {'category_slug': ['name']}
    exclude = ['image_webp']


class ProductFeatureInline(TranslationTabularInline):
    model = ProductFeature


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    exclude = ['image_webp']


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    model = Product
    list_display = ('name', 'category', 'price', 'sold', 'created_at')
    search_fields = ['name', 'description']
    inlines = [ProductFeatureInline, ProductImageInline]
    prepopulated_fields = {'product_slug': ['name']}
