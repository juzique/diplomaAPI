from django.db import models
from datetime import datetime
from django.utils.translation import gettext as _

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Coordination(models.Model):
    lon = models.DecimalField(max_digits=10,decimal_places=3)
    lat = models.DecimalField(max_digits=10,decimal_places=3)
    acc = models.DecimalField(max_digits=10,decimal_places=3)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.date)
