from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.tokens import default_token_generator

from rest_framework import serializers

from .models import User

from django.core.validators import RegexValidator
from rest_framework.exceptions import NotAuthenticated
from django.contrib.auth.hashers import make_password, check_password
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    alphanumeric = RegexValidator(
        r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
        validators=[alphanumeric]
    )

    class Meta:
        model = User
        fields = ['id', 'email', 'password']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('email', 'password')
