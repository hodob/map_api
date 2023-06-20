
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.urls import resolve


class AccountViewSet(viewsets.ViewSet):

    def list(self, request):

        # HTTP GET 요청에 대한 처리를 담당합니다.
        # 모든 사용자를 조회하여 리스트 형태로 반환하거나, 사용자 목록에 대한 필터링 또는 정렬을 수행할 수 있습니다.
        return Response("test")

    def create(self, request):
        # permission_classes = (AllowAny,)
        # HTTP POST 요청에 대한 처리를 담당합니다.
        # 새로운 사용자를 생성하기 위해 요청으로부터 받은 데이터를 사용하여 새로운 사용자를 만듭니다.
        return Response("test2")
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