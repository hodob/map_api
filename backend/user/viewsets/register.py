from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from user.serializers.customuserserializers import UserSerializer


class RegisterViewSet(viewsets.ModelViewSet):
    http_method_names = ["post"]
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "success": True,
                "userID": user.id,
                "msg": "회원가입완료",
            },
            status=status.HTTP_201_CREATED,
        )
