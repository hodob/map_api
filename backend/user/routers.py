from django.urls import path, include
from rest_framework import routers
from user.viewsets.TestViewSet import TestViewSet
from user.viewsets.account import AccountViewSet
from user.viewsets.login import LoginViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register("test", TestViewSet,basename="test")
router.register("account", AccountViewSet,basename="account")
router.register("login", LoginViewSet,basename="login")

urlpatterns = [
    path('', include(router.urls)),
]