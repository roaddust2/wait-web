from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.user import CustomUser
from .models.home import CarouselItem
from .models.product import Category, Product, ProductImage


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser


admin.site.register(CarouselItem)

admin.site.register(Category)


class ProductImageInline(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
