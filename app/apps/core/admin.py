from django.contrib import admin
from apps.core import models


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('link',)
    list_display = ('link',)
