from rest_framework import permissions
from rest_framework import viewsets

from .serializers import ProfileSerializer
from .models import UserProfile
from board.service import IsOwnerOrAdmin


class ProfileViewSet(viewsets.ModelViewSet):
    """CRUD for UserProfile model"""
    queryset = UserProfile.objects.filter()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.action in ['retrieve']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsOwnerOrAdmin]

        return [permission() for permission in permission_classes]

