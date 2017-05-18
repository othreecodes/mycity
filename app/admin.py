from django.contrib import admin
from .models import *


@admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user__first_name', 'address', 'phone_number']
    search_fields = ['phone_number', 'address']
