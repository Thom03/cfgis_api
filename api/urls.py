from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewset, ProjectViewset, MapLayerViewset


router = routers.DefaultRouter()
router.register(r'users', UserViewset)
router.register(r'projects', ProjectViewset)
router.register(r'maplayers', MapLayerViewset)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
]