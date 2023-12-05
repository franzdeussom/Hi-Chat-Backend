from django.contrib import admin

from users.models import User

admin.site.empty_value_display = "--empty--"


@admin.register(User)
class HichatUserAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "email", "phone", "age", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "gender", "account_type")
    search_fields = ("first_name", "last_name", "email")
    ordering = ("date_joined",)
    list_per_page = 25
