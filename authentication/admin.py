from django.contrib import admin
from authentication.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from listings.models import Listing


class UserAdmin(BaseUserAdmin):
    using = 'authentication_db'
    fieldsets = (
        (None, {"fields": ("password",)}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_realtor",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", )}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("name", "email", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "name", "is_staff", "is_realtor",)
    search_fields = ("name", "email")
    ordering = ("email",)

    def delete_model(self, request, obj):
        print("deleting user ...")
        Listing.objects.filter(realtor=obj.email).delete()
        obj.delete(using=self.using)
        print("user deleted ...")


admin.site.register(User, UserAdmin)
