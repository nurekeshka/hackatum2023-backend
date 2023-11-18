from apps.core.models import Image
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return str(self.name)


class Preference(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')

    class Meta:
        verbose_name = 'preference'
        verbose_name_plural = 'preferences'

    def __str__(self) -> str:
        return str(self.name)


class Ingredient(models.Model):
    MASS = 0
    FLUID = 1
    PIECE = 2

    QUANTITY_UNITS = (
        (MASS, 'gram'),
        (FLUID, 'millilitre'),
        (PIECE, 'piece')
    )

    name = models.CharField(max_length=255, verbose_name='name')
    categories = models.ManyToManyField(Category, verbose_name='categories')
    preferences = models.ManyToManyField(Preference, verbose_name='preference')

    instance_of = models.ForeignKey(
        'Ingredient', on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name='instance of')

    quantity = models.FloatField(
        verbose_name='quantity', null=True, blank=True)
    unit = models.IntegerField(
        default=None, choices=QUANTITY_UNITS,
        null=True, blank=True, verbose_name='unit')

    image = models.ForeignKey(
        Image, on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='image')

    class Meta:
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'

    def __str__(self) -> str:
        return str(self.name)
