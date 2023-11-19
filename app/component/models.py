from django.db import models
#from django.contrib.auth import

class User(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=32, unique=True)
    points = models.IntegerField(default=0)
    claimed_issues = models.ManyToManyField('Issue', blank=True)

    def __str__(self):
        self.name = self.name
        return self.name + ' ' + self.email


class Issue(models.Model):
    bool = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
