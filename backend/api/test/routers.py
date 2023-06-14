from api.test.viewsets.giveapikey import GiveApiKey
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)

router.register(r"giveapikey", GiveApiKey, basename="giveapikey")


urlpatterns = [
    *router.urls,
]