from api.test.viewsets.giveapikey import GiveApiKey
from api.test.viewsets.testapikey import TestApiKey
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)

router.register(r"giveapikey", GiveApiKey, basename="giveapikey")
router.register(r"testapikey", GiveApiKey, basename="testapikey")



urlpatterns = [
    *router.urls,
]