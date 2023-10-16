from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Profile

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["id", "email", "is_staff", "is_superuser", "is_active"]
    list_display_links = ["id", "email"]
    list_editable = ["is_active"]
    list_per_page = 10
    readonly_fields = ["last_login", "date_joined"]
    search_fields = ["email__istartswith"]
    ordering = ["email"]
    fieldsets = [
        (_("Authentication"), {"fields": ["email", "password"]}),
        (
            _("Permissions"),
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ]
            },
        ),
        (
            _("Important Dates"),
            {"classes": ["collapse"], "fields": ["last_login", "date_joined"]},
        ),
    ]
    add_fieldsets = [(None, {"fields": ["email", "password1", "password2"]})]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name"]
    list_per_page = 10
    search_fields = ["user__email__istartswith", "last_name__istartswith"]
    ordering = ["user__email"]

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("user")

    def email(self, profile):
        return profile.user.email
