from django.conf.urls import url
from .views import RegistrationAPIView, LoginAPIView


urlpatterns = [
    url('register', RegistrationAPIView.as_view()),
    url('login', LoginAPIView.as_view())
]
