from apps.components.models import Ingredient, Facility
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
    facilities = models.ManyToManyField(Facility, verbose_name='facilities')

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


class Step(models.Model):
    number = models.IntegerField(verbose_name='number')
    action = models.ForeignKey(
        Action, on_delete=models.CASCADE, verbose_name='step')

    class Meta:
        verbose_name = 'step'
        verbose_name_plural = 'steps'

    def __str__(self) -> str:
        return f'{self.number}. {self.action}'


class Recipe(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    steps = models.ManyToManyField(Step, verbose_name='steps')

    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'

    def __str__(self) -> str:
        return ''.join(str(step) for step in self.steps.order_by('number'))
