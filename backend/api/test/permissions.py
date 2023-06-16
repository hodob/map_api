from rest_framework_api_key.permissions import BaseHasAPIKey

from api.test.model import UserAPIKey

# class KeyParser:
#     def get(self, request):
#         return request.GET['apikey']
class HasUserAPIKey(BaseHasAPIKey):
    model = UserAPIKey
    # key_parser = KeyParser()