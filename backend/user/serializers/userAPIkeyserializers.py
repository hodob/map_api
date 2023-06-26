from django.contrib.auth import authenticate
from rest_framework import serializers

from user.models import UserAPIKey
from user.src.userEnum import ApiKeyCategory


class UserAPIKeySerializers(serializers.Serializer):
    user_id = serializers.IntegerField(required=False)
    key = serializers.CharField(max_length=255)
    expiration_date = serializers.CharField(max_length=255, required=False)
    category = serializers.ChoiceField(choices=[(choice.name, choice.value) for choice in ApiKeyCategory])
    is_active = serializers.BooleanField(required=False)


    class Meta:
        model = UserAPIKey
        fields = ["id","user_id", "key", "expiration_date", "category", "is_active"]

    # def validate_username(self, value):
    #     try:
    #         User.objects.get(username=value)
    #     except ObjectDoesNotExist:
    #         return value
    #     raise ValidationError({"success": False, "msg": "Username already taken."})

    # def validate_email(self, value):
    #     try:
    #         User.objects.get(email=value)
    #     except ObjectDoesNotExist:
    #         return value
    #     raise ValidationError({"success": False, "msg": "Email already taken."})

    def create(self, validated_data):
        # return UserAPIKey.objects.create_key(**validated_data)
        UserAPIKey.objects.create(**validated_data)
        return "success"
