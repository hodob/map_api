from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, name, email, password=None, **kwargs):
        # if username is None:
        #     raise TypeError("Users must have a username.")
        # if email is None:
        #     raise TypeError("Users must have an email.")

        user = self.model(name=name, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
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



