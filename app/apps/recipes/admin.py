from django.contrib import admin
from apps.recipes import models


@admin.register(models.Parameter)
class ParameterAdmin(admin.ModelAdmin):
    fields = ('name', 'unit')
    list_display = ('name', 'unit')


@admin.register(models.Process)
class ProcessAdmin(admin.ModelAdmin):
    fields = ('name', 'parameters', 'facilities', 'image')
    list_display = ('name', 'image')


@admin.register(models.Attribute)
class AttributeAdmin(admin.ModelAdmin):
    fields = ('parameter', 'value')
    list_display = ('parameter', 'value')


@admin.register(models.Action)
class ActionAdmin(admin.ModelAdmin):
    fields = ('ingredients', 'process', 'attributes', 'product')
    list_display = ('process', 'product')


@admin.register(models.Step)
class StepAdmin(admin.ModelAdmin):
    fields = ('number', 'action')
    list_display = ('number', 'action')


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ('name', 'steps')
    list_display = ('name',)
