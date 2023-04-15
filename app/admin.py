from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from modeltranslation.admin import TranslationAdmin
from .models.user import CustomUser
from .models.home import CarouselItem
from .models.product import Category, Product, ProductImage


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser


admin.site.unregister(FlatPage)

@admin.register(FlatPage)
class CustomFlatPageAdmin(TranslationAdmin, FlatPageAdmin):
    model = FlatPage


admin.site.register(CarouselItem)

admin.site.register(Category)


class ProductImageInline(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
