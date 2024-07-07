from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import househead

@admin.register(househead)
class HouseAdmin(OSMGeoAdmin):
    list_display = ('fullname', 'photo', 'tole','wardno','location','address','phone')

