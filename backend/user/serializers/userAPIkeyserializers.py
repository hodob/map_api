from django.contrib.auth import authenticate
from rest_framework import serializers

from user.src.userEnum import ApiKeyCategory


class UserAPIKeySerializers(serializers.Serializer):
    key = serializers.CharField(max_length=255)
    is_active = serializers.BooleanField()
    expiration_date = serializers.CharField(max_length=255, required=False)
    category = serializers.CharField(max_length=255)

    def validate(self, data):
        email = data.get("email", None)
        user = authenticate(username=email)
