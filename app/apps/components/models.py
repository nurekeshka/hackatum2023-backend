from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')

    def __str__(self) -> str:
        return str(self.name)


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')

    def __str__(self) -> str:
        return str(self.name)


class Preference(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')

    def __str__(self) -> str:
        return str(self.name)
