from api.authentication.viewsets.register import RegisterViewSet
from api.authentication.viewsets.login import LoginViewSet
from api.authentication.viewsets.logout import LogoutViewSet
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)
# router = routers.SimpleRouter()

# router.register(r"edit", UserViewSet, basename="user-edit")

router.register(r"register", RegisterViewSet, basename="register")

router.register(r"login", LoginViewSet, basename="login")

# router.register(r"checkSession", ActiveSessionViewSet, basename="check-session")

router.register(r"logout", LogoutViewSet, basename="logout")

urlpatterns = [
    *router.urls,
]