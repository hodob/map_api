
from rest_framework.response import Response
from rest_framework.views import APIView
from api.user.models import Test



#  단순 숫자만 바꾸는거
class test(APIView):
    def get(self, request, format=None):
        # ttt=Test(test2="test")
        # ttt.save()
        test=Test.objects.all()
        print(test)

        print("테스트")
        return Response("테스트")

