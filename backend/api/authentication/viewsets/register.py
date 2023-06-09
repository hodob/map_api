from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# from api.authentication.serializers import RegisterSerializer


class RegisterViewSet(viewsets.ModelViewSet):
# class RegisterViewSet(viewsets.ViewSet):
    http_method_names = ["post"]
    permission_classes = (AllowAny,)
    # serializer_class = RegisterSerializer
    # def create(self, request, *args, **kwargs):
    #     print(request.data)
    #     return Response("list")

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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {
                "success": True,
                "userID": user.id,
                "msg": "The user was successfully registered",
            },
            status=status.HTTP_201_CREATED,
        )
# 