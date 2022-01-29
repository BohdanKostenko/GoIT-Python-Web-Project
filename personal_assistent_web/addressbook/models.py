from django.db import models
from datetime import date


class Contact(models.Model):
    name = models.CharField(max_length=32)
    phone = models.CharField('phone', max_length=50)
    birthday = models.DateField('birthday', default=date.today)
    email = models.CharField('email', max_length=254)
    address = models.CharField('address', max_length=254)

    def __str__(self):
        return self.name


