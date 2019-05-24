from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    office = models.CharField('Posto de trabalho', max_length=50)

    def __str__(self):
        return self.office
