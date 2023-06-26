from django.urls import path, include
from rest_framework import routers

from apidata.viewsets.TestViewSet import TestViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register("test", TestViewSet,basename="test")


urlpatterns = [
    path('', include(router.urls)),
]