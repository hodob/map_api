from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


# class UserManager(BaseUserManager):
    # def create_user(self, username, email, password=None, **kwargs):
    #     """Create and return a `User` with an email, username and password."""
    #     if username is None:
    #         raise TypeError("Users must have a username.")
    #     if email is None:
    #         raise TypeError("Users must have an email.")

    #     user = self.model(username=username, email=self.normalize_email(email))
    #     user.set_password(password)
    #     user.save(using=self._db)

    #     return user

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

    #     user = self.create_user(username, email, password)
    #     user.is_superuser = True
    #     user.is_staff = True
    #     user.save(using=self._db)

    #     return user


class User(AbstractBaseUser, PermissionsMixin):
    userid = models.CharField(db_index=True, max_length=255, unique=True)
    password = models.CharField(max_length=128, blank=True)
    name=models.CharField(max_length=128, blank=True)
    email = models.EmailField(db_index=True, unique=True)
    phone=models.CharField(max_length=128, blank=True)
    address=models.CharField(max_length=128, blank=True)
    dob=models.CharField(max_length=128, blank=True)
    agreeTerms=models.CharField(max_length=128, blank=True)
    agreePrivacyPolicy=models.CharField(max_length=128, blank=True)
    agreeDataProcessing=models.CharField(max_length=128, blank=True)
    is_active=models.CharField(max_length=128, blank=True)
    date=models.CharField(max_length=128, blank=True)
    
    # username = models.CharField(db_index=True, max_length=255, unique=True)
    # email = models.EmailField(db_index=True, unique=True)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # date = models.DateTimeField(auto_now_add=True)

    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ["username"]

    # objects = UserManager()

    def __str__(self):
        return f"{self.email}"
