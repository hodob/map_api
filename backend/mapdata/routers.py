from django.urls import path, include
from rest_framework import routers
from mapdata.viewsets.TestViewSet import *

router = routers.SimpleRouter(trailing_slash=False)
# router.register("test", TestViewSet,basename="test")


urlpatterns = [
    path('', include(router.urls)),
    path('test/', TestAPIView.as_view(), name='test'),
    path('test2/', TestAPIView2.as_view(), name='test'),
]