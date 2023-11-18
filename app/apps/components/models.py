from apps.core.models import Image
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')

    def __str__(self) -> str:
        return str(self.name)


class Preference(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')

    def __str__(self) -> str:
        return str(self.name)


class Ingredient(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    categories = models.ManyToManyField(Category, verbose_name='categories')
    preferences = models.ManyToManyField(Preference, verbose_name='preference')

    instance_of = models.ForeignKey(
        'Ingredient', on_delete=models.CASCADE, verbose_name='instance of')

    image = models.ForeignKey(
        Image, on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='image')

    class Meta:
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'

    def __str__(self) -> str:
        return str(self.name)
