from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from places.models import Place


@admin.register(Place)
class PlaceAdmin(OSMGeoAdmin):
    pass
