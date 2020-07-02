import re
from django.utils.translation import ugettext_lazy as _

from rest_framework import status, generics, permissions, views
from rest_framework.generics import (
    GenericAPIView
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from rest_framework.views import APIView
from .helpers import handle_token

from .serializers import (
    LoginSerializer,
    RegistrationSerializer,
    UserSerializer
)
from .models import User
from .serializers import RegistrationSerializer
from django.contrib.auth import authenticate

from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status, views


User = get_user_model()


class RegistrationAPIView(GenericAPIView):
    """
    post:
    Signup a user.
    """
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
        except Exception as e:
            return Response({'error': 'kindly provide a {}'.format(e)})

        _user = {
            "email": email,
            "password": password
        }
        ser = RegistrationSerializer(data=_user)
        ser.is_valid(raise_exception=True)

        try:
            user = User.objects.create(email=email,
                                       password=make_password(password))
        except Exception as e:
            return Response({'error': 'User already exists', 'status': 409}, status=409)

        serializer = RegistrationSerializer(user)

        response = {
            "data": serializer.data,
            "message": "Account successfully registered.",
        }

        return Response(data=response,
                        status=status.HTTP_201_CREATED)


class LoginAPIView(GenericAPIView):
    """
    post:
    Login a user.
    """
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
        except Exception as e:
            return Response({'error': 'kindly provide a {}'.format(e)})

        try:
            user = User.objects.get(email=email)
        except Exception as e:
            return Response({'error': 'Invalid email or password', 'status': 400}, status=400)

        if check_password(password, user.password):
            token = handle_token(user)
            isAdmin = user.is_superuser
            _res = RegistrationSerializer(user)
            res = _res.data
            res['token'] = token
            res['isAdmin'] = isAdmin

            return Response(res, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid email or password', 'status': 400}, status=400)
