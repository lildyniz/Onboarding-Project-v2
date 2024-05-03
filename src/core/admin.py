from django.contrib import admin
from .models import User, Business, Direction, Region, City, Question, Answer, Page


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


class AnswerInline(admin.StackedInline):
    model = Answer


@admin.register(Question)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ['text']
    inlines = [AnswerInline]


@admin.register(Answer)
class ParameterValuesAdmin(admin.ModelAdmin):
    list_display = ['question', 'text']


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'display_questions']

    def display_questions(self, obj):
        return ', '.join([str(quest) for quest in obj.questions.all()])

    display_questions.short_description = 'Questions'