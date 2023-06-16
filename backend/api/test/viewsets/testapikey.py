from rest_framework import viewsets, status
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from ..permissions import HasUserAPIKey
from rest_framework_api_key.models import BaseAPIKeyManager
from rest_framework_api_key.crypto import KeyGenerator

from rest_framework_api_key.models import APIKey
from api.test.model import UserAPIKey
from datetime import datetime, timedelta
import pytz
from api.user.models import UserAPIKeyManager


# class OrganizationAPIKeyManager(BaseAPIKeyManager):
# class OrganizationAPIKeyManager(UserAPIKeyManager):
#     key_generator = KeyGenerator(prefix_length=4, secret_key_length=32)  # Default values

class TestApiKey(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,HasUserAPIKey,)
    def list(self, request, *args, **kwargs):

        return Response("test")
