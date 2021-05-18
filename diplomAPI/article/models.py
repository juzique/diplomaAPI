from django.db import models
from datetime import datetime
from django.utils.translation import gettext as _

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Coordinations(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    lon = models.DecimalField(max_digits=10,decimal_places=3)
    lat = models.DecimalField(max_digits=10,decimal_places=3)
    acc = models.DecimalField(max_digits=10,decimal_places=3)
    #speed = models.DecimalField(max_digits=10,decimal_places=3)
    date = models.DateTimeField(default=datetime.now, blank=True)
    #userid = models.CharField(max_length=100)

    class Meta:
        verbose_name= 'Coordinations'
        verbose_name_plural= 'Coordinations'

    def __str__(self):
        return '%s: %s, %s' % (self.username, self.lon, self.lat)
