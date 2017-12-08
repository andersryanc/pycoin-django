from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    ssn = models.CharField(max_length=10)
    homephone = models.CharField(max_length=20)
    cellphone = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
