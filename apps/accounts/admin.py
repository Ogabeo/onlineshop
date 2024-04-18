from django.contrib import admin
from .models import User, UserResetPasswordCode

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id', 'username', 'first_name', 'last_name', 'email')
    list_display_links=('id', 'username')
    search_fields=('username', 'first_name', 'last_name', 'email')

@admin.register(UserResetPasswordCode)
class UserResetPasswordCodeAdmin(admin.ModelAdmin):
    list_display=('id', 'code', 'email', 'expiration_time', 'is_confirmation',)
    list_display_links=('id', 'code', 'email',)



