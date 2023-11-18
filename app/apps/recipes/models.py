from apps.components.models import Ingredient
from apps.core.models import Image
from django.db import models


class Parameter(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    unit = models.CharField(max_length=255, verbose_name='unit')

    class Meta:
        verbose_name = 'parameter'
        verbose_name_plural = 'parameters'

    def __str__(self) -> str:
        return str(self.name)


class Process(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    parameters = models.ManyToManyField(Parameter, verbose_name='parameter')

    image = models.ForeignKey(
        Image, on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='image')

    class Meta:
        verbose_name = 'process'
        verbose_name_plural = 'processes'

    def __str__(self) -> str:
        return str(self.name)


class Attribute(models.Model):
    parameter = models.ForeignKey(
        Parameter, on_delete=models.CASCADE, verbose_name='parameter')
    value = models.CharField(max_length=255, verbose_name='value')

    class Meta:
        verbose_name = 'attribute'
        verbose_name_plural = 'attributes'

    def __str__(self) -> str:
        return f'{self.parameter}: {self.value}'


class Action(models.Model):
    ingredients = models.ManyToManyField(
        Ingredient, verbose_name='ingredients',
        related_name='ingredients')

    attributes = models.ManyToManyField(
        Attribute, verbose_name='attributes')

    product = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, verbose_name='product',
        related_name='product')

    process = models.ForeignKey(
        Process, on_delete=models.CASCADE, verbose_name='process')

    class Meta:
        verbose_name = 'action'
        verbose_name_plural = 'actions'

    def __str__(self) -> str:
        return ' '.join((
            f'Process of {self.process.name}',
            f'{", ".join(map(str, self.ingredients.all()))}',
            f'to make {self.product.name}'
        ))


class Recipe(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    actions = models.ManyToManyField(Action, verbose_name='actions')

    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'

    def __str__(self) -> str:
        return ''.join(str(action) for action in self.actions.all())
