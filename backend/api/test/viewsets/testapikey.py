from rest_framework import viewsets
from rest_framework.response import Response
from ..permissions import HasUserAPIKey

class TestApiKey(viewsets.ModelViewSet):

    permission_classes = (HasUserAPIKey,)
    def list(self, request, *args, **kwargs):

        return Response("접근허가")
