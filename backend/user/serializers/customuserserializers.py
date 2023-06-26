from rest_framework import serializers

from user.models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=4, max_length=255, write_only=True)
    name = serializers.CharField(max_length=255, required=False)
    phone = serializers.CharField(max_length=255, required=False)
    address = serializers.CharField(max_length=255, required=False)
    dob = serializers.CharField(max_length=255, required=False)
    agreeTerms = serializers.BooleanField(required=False)
    agreePrivacyPolicy = serializers.BooleanField(required=False)
    agreeDataProcessing = serializers.BooleanField(required=False)

    class Meta:
        model = User
        fields = ["id", "name", "email", "password", "phone", "address", "dob", "agreeTerms", "agreePrivacyPolicy", "agreeDataProcessing"]



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
        return User.objects.create_user(**validated_data)
