from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from rest_framework_api_key.models import BaseAPIKeyManager

class UserAPIKeyManager(BaseAPIKeyManager):
    def get_usable_keys(self) -> models.QuerySet:
        return super().get_usable_keys().filter(user__retired=False)


class UserManager(BaseUserManager):
    def create_user(self, name, email, password=None, **kwargs):
        """Create and return a `User` with an email, username and password."""
        # if username is None:
        #     raise TypeError("Users must have a username.")
        # if email is None:
        #     raise TypeError("Users must have an email.")

        user = self.model(name=name, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    # def create_superuser(self, username, email, password):
    #     """
    #     Create and return a `User` with superuser (admin) permissions.
    #     """
    #     if password is None:
    #         raise TypeError("Superusers must have a password.")
    #     if email is None:
    #         raise TypeError("Superusers must have an email.")
    #     if username is None:
    #         raise TypeError("Superusers must have an username.")
    #
    #     user = self.create_user(username, email, password)
    #     user.is_superuser = True
    #     user.is_staff = True
    #     user.save(using=self._db)
    #     return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(db_index=True, unique=True)
    password = models.CharField(max_length=128, blank=True)
    name=models.CharField(max_length=128, blank=True)
    phone=models.CharField(max_length=128, blank=True)
    address=models.CharField(max_length=128, blank=True)
    dob=models.CharField(max_length=128, blank=True)
    agreeTerms=models.BooleanField(max_length=128 ,null=True,blank=True)
    agreePrivacyPolicy=models.BooleanField(max_length=128 ,null=True,blank=True, default=True)
    agreeDataProcessing=models.BooleanField(max_length=128,null=True,blank=True )
    is_active=models.BooleanField(max_length=128, default=True)
    is_admin=models.BooleanField(max_length=128, default=False)
    date_join=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(null=True,blank=True)
    is_staff=models.BooleanField(max_length=128, default=False)


    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"


class Test(models.Model):
    test=models.CharField(max_length=128, blank=True)
