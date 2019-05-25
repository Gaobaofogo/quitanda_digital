from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Employee(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    office = models.CharField('Posto de trabalho', max_length=50)

    def __str__(self):
        return self.office

    class Meta:
        permissions = (('superadmin', 'Super Admin'), )
