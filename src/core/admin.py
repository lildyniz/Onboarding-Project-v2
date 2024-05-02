from django.contrib import admin
from .models import User, Business, Direction


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'business']


class DirectionInline(admin.StackedInline):
    model = Direction


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ['business_type']
    inlines = [DirectionInline]


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ['direction', 'business']