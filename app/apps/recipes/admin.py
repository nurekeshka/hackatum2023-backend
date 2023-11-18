from django.contrib import admin
from apps.recipes import models


@admin.register(models.Process)
class ProcessAdmin(admin.ModelAdmin):
    fields = ('name', 'image')
    list_display = ('name', 'image')


@admin.register(models.Action)
class ActionAdmin(admin.ModelAdmin):
    fields = ('ingredients', 'process', 'outcome')
    list_display = ('process', 'outcome')


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ('name', 'actions')
    list_display = ('name',)
