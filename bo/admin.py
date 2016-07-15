from django.contrib import admin

from models import *
from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

class AppUserAdmin(OSMGeoAdmin):
    fieldsets = [
        (None, {'fields': ['email','online','lastConnexionDate','location','password','firstName','lastName','sex']}),
    ]
    list_display = ('email','online','lastConnexionDate','location','password','firstName','lastName','sex',)
    list_filter = ('online','sex',)
    ordering = ('email','online', 'lastConnexionDate',)
    search_fields = ('email','firstName','lastName',)

class CitiesAdmin(OSMGeoAdmin):
    fieldsets = [
        (None, {'fields': ['name','isoCode','location']}),
    ]
    list_display = ('name','isoCode','location',)
    list_filter = ('name','isoCode',)
    ordering = ('name','isoCode',)
    search_fields = ('name','isoCode',)

class FavoritesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['citiesId','userId']}),
    ]
    list_display = ('citiesId','userId',)
    list_filter = ('userId','citiesId')
    ordering = ('userId','citiesId',)
    search_fields = ('userId','citiesId',)

admin.site.register(AppUser,AppUserAdmin)
admin.site.register(Cities,CitiesAdmin)
admin.site.register(Favorites,FavoritesAdmin)
