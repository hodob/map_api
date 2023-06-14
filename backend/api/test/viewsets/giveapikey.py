from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from api.authentication.serializers.registerserializers import RegisterSerializer

from api.user.models import Test
from rest_framework_api_key.models import BaseAPIKeyManager
from rest_framework_api_key.crypto import KeyGenerator

from rest_framework_api_key.models import APIKey
from api.test.model import UserAPIKey
from datetime import datetime, timedelta


class OrganizationAPIKeyManager(BaseAPIKeyManager):
    key_generator = KeyGenerator(prefix_length=8, secret_key_length=32)  # Default values

class GiveApiKey(viewsets.ModelViewSet):

    # http_method_names = ["post"]
    permission_classes = (IsAuthenticated,)
    def list(self, request, *args, **kwargs):

        keys = UserAPIKey.objects.all()
        # for key in keys:
        #     if key.name == username:
        #         key.delete()
        #         break
        # # api_key, key = APIKey.objects.create_key(name=request.user.username)
        api_key, key = UserAPIKey.objects.create_key(name="지정호")
        expires = datetime.now() + timedelta(days=90)
        api_key.expiry_date = expires
        # api_key.save()
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
    
