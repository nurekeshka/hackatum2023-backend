from django.contrib import admin
from apps.components import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)


@admin.register(models.Preference)
class PreferenceAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)


@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    fields = ('name', ('categories', 'preferences'), 'instance_of', 'image')
    list_display = ('name', 'instance_of', 'image')
