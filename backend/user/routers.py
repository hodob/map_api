from django.urls import path, include
from rest_framework import routers
from user.viewsets.TestViewSet import TestViewSet
from user.viewsets.account import AccountViewSet
from user.viewsets.login import LoginViewSet
from user.viewsets.logout import LogoutViewSet
from user.viewsets.register import RegisterViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register("test", TestViewSet,basename="test")
router.register("account", AccountViewSet,basename="account")
router.register("login", LoginViewSet,basename="login")
router.register("register", RegisterViewSet,basename="login")
router.register("logout", LogoutViewSet,basename="login")

urlpatterns = [
    path('', include(router.urls)),
]