from django.contrib import admin
from .models import (Company, Technology, Position,
                     Country, City, Street, Location)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'location')
    search_fields = ('name', 'location__country__name', 'location__city__name', 'location__street__name')
    list_filter = ('location__country', 'location__city')
    ordering = ('name',)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('technology_name',)
    search_fields = ('technology_name',)
    ordering = ('technology_name',)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country__name')
    list_filter = ('country',)
    ordering = ('name',)


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street')
    search_fields = ('country__name', 'city__name', 'street__name')
    list_filter = ('country', 'city')
    ordering = ('country', 'city', 'street')
