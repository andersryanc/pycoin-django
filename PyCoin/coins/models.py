from django.db import models


class Coin(models.Model):
    description = models.CharField(max_length=100)
    value = models.FloatField()

    def __str__(self):
        return self.description
