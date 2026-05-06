# users/admin.py
from django.contrib import admin
from users.models import CustomUser, Profile, Role, Otp

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'created_at')
    list_filter = ('is_active', 'role', 'created_at')
    search_fields = ('username', 'email')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone_number')
    search_fields = ('user__username', 'first_name', 'last_name')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

@admin.register(Otp)
class OtpAdmin(admin.ModelAdmin):
    list_display = ('user', 'otp', 'is_used', 'expires_at', 'created_at')
    list_filter = ('is_used',)