from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import User, Project, MapLayers
from api.serializers import UserSerializer, ProjectSerializer, MapLayerSerializer
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    """Applying permissions to this Viewset."""

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


class ProjectViewset(viewsets.ModelViewSet):
    """Viewset for Project."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    """Applying permissions to this Viewset."""

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        elif self.action == 'list':
            permission_classes = [IsLoggedInUserOrAdmin]

        return [permission() for permission in permission_classes]


class MapLayerViewset(viewsets.ModelViewSet):
    """Viewset for Maplayers."""
    queryset = MapLayers.objects.all()
    serializer_class = MapLayerSerializer

    """Applying permissions to this Viewset."""

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        elif self.action == 'list':
            permission_classes = [IsLoggedInUserOrAdmin]

        return [permission() for permission in permission_classes]
