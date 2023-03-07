from django.contrib import admin
from yumyay.models import Cuisine, Recipe
from yumyay.models import UserProfile


# Register your models here.


class CuisineAdmin(admin.ModelAdmin):
    list_display = ('name',)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(UserProfile)

