import logging

from rest_framework import permissions
from rest_framework import viewsets

from .serializers import (
    AdvertSerializer, AdvertDetailSerializer,
    ReviewCreateSerializer, AdvertCreateSerializer
)
from .models import Advert, Review
from Services.board import (
    permissions as service_p, filters as service_f
)

logger = logging.getLogger(__name__)


class AdvertViewSet(viewsets.ModelViewSet):
    """Full CRUD actions for Advert model"""

    logger.debug('AdvertViewSet')

    queryset = Advert.objects.all()
    filterset_class = service_f.AdvertFilter

    def get_permissions(self):
        """Selects permission depending on action"""
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        elif self.action in ['update', 'destroy']:
            permission_classes = [service_p.IsOwnerOrAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        """Selects serializer depending on action"""
        if self.action == 'list':
            serializer_class = AdvertSerializer
        elif self.action == 'create':
            serializer_class = AdvertCreateSerializer
        else:
            serializer_class = AdvertDetailSerializer

        return serializer_class


class ReviewViewSet(viewsets.ModelViewSet):
    """ViewSet for create & destroy actions for Review objects"""

    logger.debug('ReviewViewSet')

    queryset = Review.objects.filter()
    serializer_class = ReviewCreateSerializer

    def get_permissions(self):
        """Selects permission depending on action"""
        if self.action in ['create']:
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['destroy', 'update']:
            permission_classes = [service_p.IsOwnerOrAdmin]

        return [permission() for permission in permission_classes]
