from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'phone_number']
    search_fields = ['phone_number', 'address']


admin.site.register(Profile, ProfileAdmin)
