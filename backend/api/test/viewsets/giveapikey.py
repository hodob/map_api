from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# from api.test.model import UserAPIKey

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
        api_key, key = UserAPIKey.objects.create_key(user_id=self.request.user.id, name=self.request.user.name)
        #  키 만료 없음
        # expires = datetime.now(tz=pytz.timezone('Asia/Seoul')) + timedelta(days=90)
        # api_key.expiry_date = expires
        # api_key.save()
        # return Response({'apikey': key, 'expires': expires}, status=status.HTTP_200_OK)
        return Response({'apikey': key})
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
    
