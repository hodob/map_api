import secrets
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from user.models import UserAPIKey
from user.serializers.userAPIkeyserializers import UserAPIKeySerializers
from user.src.encrypt_utils import EncryptUtils
from rest_framework import status

from user.src.userEnum import ApiKeyCategory


class UserApiKeyViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserAPIKeySerializers

    def list(self, request):
        user_id = request.user.id
        queryset = UserAPIKey.objects.filter(user_id=user_id)
        serializer = UserAPIKeySerializers(queryset, many=True)
        data = serializer.data
        print(data)
        # keys = [(item['key'], item['category']) for item in data]
        keys = [{'key': item['key'], 'category': item['category']} for item in data]
        print(keys)

        # return Response(data.get('key'))
        return Response(keys,status=status.HTTP_200_OK)


    def create(self, request):
        key = EncryptUtils.encrypt(secrets.token_urlsafe(32))
        data = {'key': key, 'category': ApiKeyCategory.INU.name, "user_id": request.user.id}
        del key
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"key": EncryptUtils.decrypt(serializer.validated_data['key'])}, status=status.HTTP_200_OK)


    def retrieve(self, request, pk=None):
        # HTTP GET 요청에 대한 처리를 담당합니다.
        # 특정 사용자를 조회하기 위해 요청에서 전달된 고유 식별자(primary key)를 사용하여 해당 사용자의 상세 정보를 반환합니다.
        pass

    def update(self, request, pk=None):
        # HTTP PUT 요청에 대한 처리를 담당합니다.
        # 특정 사용자의 정보를 업데이트하기 위해 요청에서 전달된 데이터를 사용하여 해당 사용자의 필드 값을 변경합니다.
        pass

    def partial_update(self, request, pk=None):
        # HTTP PATCH 요청에 대한 처리를 담당합니다.
        # 특정 사용자의 일부 정보만 업데이트하기 위해 요청에서 전달된 데이터를 사용하여 해당 사용자의 필드 값을 부분적으로 변경합니다.
        pass

    def destroy(self, request, pk=None):
        # HTTP DELETE 요청에 대한 처리를 담당합니다.
        # 특정 사용자를 삭제하기 위해 요청에서 전달된 고유 식별자(primary key)를 사용하여 해당 사용자를 삭제합니다.
        pass
