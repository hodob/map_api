from rest_framework import viewsets
from rest_framework.response import Response
from mapdata.src.db_connect import get_database_connection


class TestViewSet(viewsets.ViewSet):

# 35.2397951,129.0814828
    def list(self, request):
        conn = get_database_connection()
        cur = conn.cursor()
        select_data = str("select * from inu_obs_mi where (id, obs_time) in (select id ,max(obs_time) from inu_obs_mi group by id)")
        cur.execute(select_data)
        data = cur.fetchall()
        cur.close()
        return Response(data)


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