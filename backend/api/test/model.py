from django.db import models
from django.contrib.auth import get_user_model
from rest_framework_api_key.models import AbstractAPIKey
from api.user.models import User
class UserAPIKey(AbstractAPIKey):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="apikey")

    # class Meta(AbstractAPIKey.Meta):
    #     ordering = ['user']
    #     verbose_name = "User API key"