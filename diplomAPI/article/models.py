from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Coordinations(models.Model):
    lon = models.DecimalField(max_digits=10,decimal_places=3)
    lat = models.DecimalField(max_digits=10,decimal_places=3)
    #acc = models.DecimalField(max_digits=10,decimal_places=3)
    date = models.DateField()
