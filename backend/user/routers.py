from django.urls import path, include
from rest_framework import routers
from user.viewsets.TestViewSet import TestViewSet

router = routers.SimpleRouter()
router.register("test", TestViewSet,basename="test")
router.register("account", TestViewSet,basename="account")
router.register("login", TestViewSet,basename="login")

urlpatterns = [
    path('', include(router.urls)),
]