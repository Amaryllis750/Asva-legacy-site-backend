from django.contrib import admin
from unfold import admin as UnfoldAdmin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(UnfoldAdmin.ModelAdmin):
    list_display = ("user", "reference_code")
    search_fields = ("user__username", "user__email", "reference_code")

