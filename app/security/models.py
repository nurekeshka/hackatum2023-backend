from django.db import models
# import sys
# sys.path.insert(0, 'C:/Users/ПК/PycharmProjects/hackatum2023-backend/app')
class Security(models.Model):
    yt_token = models.CharField(max_length=64, unique=True)
    session_token = models.CharField(max_length=64)

    def __str__(self):
        return "%s the user has this yt_token: %s" % (self.name, self.yt_token)
