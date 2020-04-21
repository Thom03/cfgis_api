from django.conf.urls import url,include
from rest_framework import routers
from api.views import UserViewset


router = routers.DefaultRouter()
router.register(r'users', UserViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
]