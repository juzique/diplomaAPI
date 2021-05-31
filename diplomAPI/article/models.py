from django.db import models
from datetime import datetime
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _

# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, email, username, password, **extra_fields):

        # Create and save a user with the given username, email and password.

        if not email:
            raise ValueError('The given email must be set')
        if not username:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(
            email=email, username=username, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email, username, password, **extra_fields
        )

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(
            email, username, password, **extra_fields
        )

class Users(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
    )
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    class Meta:
        verbose_name= 'Users'
        verbose_name_plural= 'Users'

    def __str__(self):
        return self.username

class Coordinations(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
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
