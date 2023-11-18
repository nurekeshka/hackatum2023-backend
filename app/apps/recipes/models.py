from apps.components.models import Ingredient
from apps.core.models import Image
from django.db import models


class Process(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')

    image = models.ForeignKey(
        Image, on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='image')

    class Meta:
        verbose_name = 'process'
        verbose_name_plural = 'processes'

    def __str__(self) -> str:
        return str(self.name)


class Action(models.Model):
    ingredients = models.ManyToManyField(
        Ingredient, verbose_name='ingredients',
        related_name='ingredients')

    outcome = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, verbose_name='outcome',
        related_name='outcome')

    process = models.ForeignKey(
        Process, on_delete=models.CASCADE, verbose_name='process')

    class Meta:
        verbose_name = 'action'
        verbose_name_plural = 'actions'

    def __str__(self) -> str:
        return ' '.join((
            f'Process of {self.process.name}',
            f'{", ".join(map(str, self.ingredients.all()))}',
            f'to make {self.outcome.name}'
        ))


class Recipe(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    actions = models.ManyToManyField(Action, verbose_name='actions')

    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'

    def __str__(self) -> str:
        return ''.join(str(action) for action in self.actions.all())
