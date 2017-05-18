from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'phone_number']
    search_fields = ['phone_number', 'address']


admin.site.register(Profile, ProfileAdmin)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['owner', 'name', 'location', 'place_type']
    list_filter = ['place_type']
    search_fields = ['name', 'location']


admin.site.register(Place, PlaceAdmin)
