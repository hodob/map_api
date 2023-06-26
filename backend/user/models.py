from datetime import timezone
from enum import Enum

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from user.src.userEnum import ApiKeyCategory


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, name, email, password=None, **kwargs):
        # if username is None:
        #     raise TypeError("Users must have a username.")
        # if email is None:
        #     raise TypeError("Users must have an email.")

        user = self.model(name=name, email=self.normalize_email(email))
        user.set_password (password)
        user.save(using=self._db)
        return user
class KeyManager(models.Manager):

    def create_key(self, **kwargs):
        key = self.create(**kwargs)
        return key

    def active_keys(self):
        return self.filter(is_active=True)

    def expired_keys(self):
        return self.filter(is_active=True, expiration_date__lt=models.timezone.now().date())

    def deactivate_all(self):
        self.update(is_active=False)

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(db_index=True, unique=True)
    password = models.CharField(max_length=128, blank=True)
    name = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=128, blank=True)
    address = models.CharField(max_length=128, blank=True)
    dob = models.CharField(max_length=128, blank=True)
    agreeTerms = models.BooleanField(max_length=128, null=True, blank=True)
    agreePrivacyPolicy = models.BooleanField(max_length=128, null=True, blank=True, default=True)
    agreeDataProcessing = models.BooleanField(max_length=128, null=True, blank=True)
    is_active = models.BooleanField(max_length=128, default=True)
    date_join = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"


class ActiveSession(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)



class UserAPIKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    create_date = models.DateField(auto_now=True)
    expiration_date = models.DateField(null=True)
    category = models.CharField(max_length=20, choices=[(status.value, status.value) for status in ApiKeyCategory])

    objects = KeyManager()
    def __str__(self):
        return self.key

    def is_expired(self):
        return self.expiration_date < timezone.now().date()

    def deactivate(self):
        self.is_active = False
        self.save()

