# common/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,  PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

class Company(models.Model):
    name = models.CharField(max_length=255)
    database_name = models.CharField(max_length=255, unique=True)
    db_user = models.CharField(max_length=255)
    db_password = models.CharField(max_length=255)
    db_host = models.CharField(max_length=255)
    db_port = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email'),max_length=100, unique=True)
    username = models.CharField(max_length=255, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='users', null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email is the USERNAME_FIELD, so it should not be included in REQUIRED_FIELDS

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        indexes = [
            models.Index(fields=['username', 'email', 'company'])
        ]
