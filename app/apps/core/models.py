from django.db import models


class Image(models.Model):
    link = models.URLField(verbose_name='link')

    def __str__(self) -> str:
        return str(self.link)

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
