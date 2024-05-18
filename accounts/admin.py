from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUserModel
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    model = CustomUserModel
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("age",)}),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("age",)}),
    )
    list_display = ["username", "email", "age", "is_staff"]


admin.site.register(CustomUserModel, CustomUserAdmin)
