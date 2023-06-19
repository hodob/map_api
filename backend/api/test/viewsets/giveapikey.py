from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from ..permissions import HasUserAPIKey
from api.authentication.serializers.registerserializers import RegisterSerializer

from api.user.models import Test
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

class GiveApiKey(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    def list(self, request, *args, **kwargs):

        keys = UserAPIKey.objects.all()
        for key in keys:
            if key.user_id == self.request.user.id:
                key.delete()
                break
        # # api_key, key = APIKey.objects.create_key(name=request.user.username)
        api_key, key = UserAPIKey.objects.create_key(user_id=self.request.user.id, name=self.request.user.name)
        expires = datetime.now(tz=pytz.timezone('Asia/Seoul')) + timedelta(days=90)
        api_key.expiry_date = expires
        api_key.save()
        return Response({'apikey': key, 'expires': expires}, status=status.HTTP_200_OK)
        # return Response("test")

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()
    #
    #     return Response(
    #         {
    #             "success": True,
    #             "userID": user.id,
    #             "msg": "The user was successfully registered",
    #         },
    #         status=status.HTTP_201_CREATED,
    #     )
    
    # def retrieve(self, request, pk=None):
    #     return Response("list")

    # def update(self, request, pk=None):
    #     return Response("list")

    # def partial_update(self, request, pk=None):
    #      return Response("list")

    # def destroy(self, request, pk=None):
    #     return Response("list")
    # http_method_names = ["post"]
    # permission_classes = (AllowAny,)
    # serializer_class = RegisterSerializer
    
