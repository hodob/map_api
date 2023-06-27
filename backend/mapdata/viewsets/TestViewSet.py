from rest_framework.views import APIView
from rest_framework.response import Response

from mapdata.src.db_quary import DatabaseQuery


class TestAPIView(APIView):
    def get(self, request):
        DBQuery = DatabaseQuery()  # Create an instance of DatabaseQuery
        test = DBQuery.getallmapdata()
        return Response(test)


class TestAPIView2(APIView):
    def get(self, request):
        DBQuery = DatabaseQuery()  # Create an instance of DatabaseQuery
        test = DBQuery.getallmapdata3()
        return Response(test)