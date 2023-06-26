from rest_framework import viewsets
from rest_framework.response import Response
import psycopg2 as psycopg
from user.models import UserAPIKey


class TestViewSet(viewsets.ViewSet):


    def list(self, request):
        conn = psycopg.connect(host='jjjteam.duckdns.org', dbname='tp_db', user='postgres', password='wjdgh7578@',
                               port=5432)
        cur = conn.cursor()
        apikey= request.GET['apikey']
        tm1 = request.GET['tm1']
        tm2 = request.GET['tm2']
        print(apikey)
        select_data = str("SELECT * FROM public.inu_obs_mi WHERE obs_time BETWEEN '%s' AND '%s' ; " % (tm1, tm2))
        # SELECT * FROM public.inu_obs_mi WHERE obs_time BETWEEN '2022-07-22 17:50:45.629947' AND '2022-07-22 17:51:35.803452' ;
        cur.execute(select_data)
        data = cur.fetchall()

        # Convert the data to a list of dictionaries
        columns = [desc[0] for desc in cur.description]
        print(columns)
        print(data)
        data_dicts = [dict(zip(columns, row)) for row in data]
        for row in data:
            row_list = list(row)
            for i in row_list:
                # if type(i) is datetime.datetime:
                #     row_list[row_list.index(i)]=str(i)
                row_list[row_list.index(i)] = str(i)
            row = tuple(row_list)
        cur.close()

        return Response(data_dicts)
        return Response({"message": "Hello, world!"})
        pass

    def create(self, request):
        # HTTP POST 요청에 대한 처리를 담당합니다.
        # 새로운 사용자를 생성하기 위해 요청으로부터 받은 데이터를 사용하여 새로운 사용자를 만듭니다.
        pass

    def retrieve(self, request, pk=None):
        # HTTP GET 요청에 대한 처리를 담당합니다.
        # 특정 사용자를 조회하기 위해 요청에서 전달된 고유 식별자(primary key)를 사용하여 해당 사용자의 상세 정보를 반환합니다.
        pass

    def update(self, request, pk=None):
        # HTTP PUT 요청에 대한 처리를 담당합니다.
        # 특정 사용자의 정보를 업데이트하기 위해 요청에서 전달된 데이터를 사용하여 해당 사용자의 필드 값을 변경합니다.
        pass

    def partial_update(self, request, pk=None):
        # HTTP PATCH 요청에 대한 처리를 담당합니다.
        # 특정 사용자의 일부 정보만 업데이트하기 위해 요청에서 전달된 데이터를 사용하여 해당 사용자의 필드 값을 부분적으로 변경합니다.
        pass

    def destroy(self, request, pk=None):
        # HTTP DELETE 요청에 대한 처리를 담당합니다.
        # 특정 사용자를 삭제하기 위해 요청에서 전달된 고유 식별자(primary key)를 사용하여 해당 사용자를 삭제합니다.
        pass