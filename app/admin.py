from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.user import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser


admin.site.register(CustomUser, UserAdmin)
