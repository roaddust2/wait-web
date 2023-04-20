from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models.user import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from .models.home import CarouselItem
from .models.product import Category, Product, ProductImage


# Customized User

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser


# Internalized flatpages

admin.site.unregister(FlatPage)


@admin.register(FlatPage)
class CustomFlatPageAdmin(TranslationAdmin, FlatPageAdmin):
    model = FlatPage


# App's models register

@admin.register(CarouselItem)
class CarouselAdmin(TranslationAdmin):
    model = CarouselItem


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    model = Category


class ProductImageInline(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(TranslationAdmin, admin.ModelAdmin):
    inlines = [ProductImageInline]
