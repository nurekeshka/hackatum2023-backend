from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=32, unique=True)
    points = models.IntegerField(default=0)
    claimed_issues = models.ForeignKey('Issue', on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'taken': True},
        related_name='active_issue_for_user')

    def __str__(self):
        return self.name + ' ' + self.email+ ' ' + str(self.id)


class Issue(models.Model):
    taken = models.BooleanField(default=False)
    title = models.CharField(max_length=64)
    description = models.TextField()
    def __str__(self):
        return self.title
