
from rest_framework.response import Response
from rest_framework.views import APIView

#  단순 숫자만 바꾸는거
class test(APIView):
    def get(self, request, format=None):
        
        print("테스트")
        return Response("테스트")

