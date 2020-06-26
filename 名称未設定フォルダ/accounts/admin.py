from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('nickname','image')}),)
    list_display = ['username', 'email', 'nickname','image']

# Register your models here.
admin.site.register(User, CustomUserAdmin)
