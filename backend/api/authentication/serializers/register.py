# from rest_framework import serializers
# from rest_framework.exceptions import ValidationError
# from django.core.exceptions import ObjectDoesNotExist
# from api.user.models import User


# class RegisterSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(required=True)
#     password = serializers.CharField(min_length=4, max_length=255, write_only=True)
#     name = serializers.CharField(max_length=255, required=True)
#     phone = serializers.CharField(max_length=255, required=True)
#     address = serializers.CharField(max_length=255, required=True)
#     dob = serializers.CharField(max_length=255, required=True)
#     agreeTerms = serializers.CharField(max_length=255, required=True)
#     agreePrivacyPolicy = serializers.CharField(max_length=255, required=True)
#     agreeDataProcessing = serializers.CharField(max_length=255, required=True)
#     is_active = serializers.BooleanField(default=True)
#     is_admin = serializers.BooleanField(default=False)
#     date_join = serializers.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         model = User
#         fields = ["id", "name", "email", "password", "phone", "address", "dob", "agreeTerms", "agreePrivacyPolicy", "agreeDataProcessing", "is_active", "is_admin", "date_join"]
    
#     # password = serializers.CharField(min_length=4, max_length=128, write_only=True)
#     # username = serializers.CharField(max_length=255, required=True)
#     # email = serializers.EmailField(required=True)

#     # class Meta:
#     #     model = User
#     #     fields = ["id", "username", "password", "email", "is_active", "date"]

#     # def validate_username(self, value):
#     #     try:
#     #         User.objects.get(username=value)
#     #     except ObjectDoesNotExist:
#     #         return value
#     #     raise ValidationError({"success": False, "msg": "Username already taken."})



#     # def validate_email(self, value):
#     #     try:
#     #         User.objects.get(email=value)
#     #     except ObjectDoesNotExist:
#     #         return value
#     #     raise ValidationError({"success": False, "msg": "Email already taken."})

#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)
