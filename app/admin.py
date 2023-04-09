from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.user import CustomUser
from .models.home import CarouselItem


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser


admin.site.register(CarouselItem)
