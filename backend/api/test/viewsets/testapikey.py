from rest_framework import viewsets
from rest_framework.response import Response
# from ..permissions import HasUserAPIKey
# from api.test.model import UserAPIKey


class TestApiKey(viewsets.ModelViewSet):

    # permission_classes = (HasUserAPIKey,)
    def list(self, request, *args, **kwargs):
        user = request.user  # 현재 로그인된 사용자
        # api_key = UserAPIKey.objects.get_from_key("SYT5Stad.mfex5LfxbyAtu4uHnbyduJ662mBN1dX9")
        # print(api_key.hashed_key)

        return Response("접근허가")
