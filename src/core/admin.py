from django.contrib import admin
from .models import User, Business, Direction, Region, City


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'business']


class DirectionInline(admin.StackedInline):
    model = Direction

class CityInline(admin.StackedInline):
    model = City

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ['business_type']
    inlines = [DirectionInline]


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ['direction', 'business']


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['region']
    cities = [CityInline]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['city', 'region']