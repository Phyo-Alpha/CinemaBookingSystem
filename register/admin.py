from typing import Any
from django.contrib import admin
from .models import User, UserProfile

#   DO NOT REPLACE THE FOLLOWING!
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_profile_name', 'display_suspension_status')
    list_filter = ('id', 'user_profile_name')
    search_fields = ('id', 'user_profile_name')
    ordering = ('id', 'user_profile_name')

    def display_suspension_status(self, obj):
        if obj.suspend:
            return 'Suspended'
        else:
            return 'Active'
    display_suspension_status.short_description = 'Status'
    display_suspension_status.admin_order_field = 'suspend'

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_type_id', 'display_suspension_status')
    list_filter = ('user_type_id',)
    search_fields = ('username', 'user_type_id')
    ordering = ('username', 'user_type_id')

    def display_suspension_status(self, obj):
        if obj.is_active == False:
            return 'Suspended'
        else:
            return 'Active'
    display_suspension_status.short_description = 'Status'
    display_suspension_status.admin_order_field = 'is_active'

class CustomUserAdmin(UserAdmin):
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
