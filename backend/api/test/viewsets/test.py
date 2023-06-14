from rest_framework_api_key.models import BaseAPIKeyManager
from rest_framework_api_key.crypto import KeyGenerator
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from api.authentication.models.active_session import ActiveSession

class OrganizationAPIKeyManager(BaseAPIKeyManager):
    key_generator = KeyGenerator(prefix_length=8, secret_key_length=32)  # Default values
    print(key_generator)
class LogoutViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        print(OrganizationAPIKeyManager.key_generator)

        return Response(
            "good"
        )

