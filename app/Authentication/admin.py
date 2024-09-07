from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
	list_display = ('email', 'name', 'is_staff', 'is_active', 'last_login')
	ordering = ('email', 'id',)
	list_filter = ('is_active', 'is_staff')
	search_fields = ('email', 'name')

admin.site.register(User, CustomUserAdmin)