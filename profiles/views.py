from rest_framework import permissions
from rest_framework import viewsets

from .serializers import CreateProfileSerializer
from .models import UserProfile
from Services.board.permissions import IsOwnerOrAdmin


class ProfileViewSet(viewsets.ModelViewSet):
    """CRUD for UserProfile model"""
    queryset = UserProfile.objects.all()
    serializer_class = CreateProfileSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def get_permissions(self):
        if self.action in ['retrieve', 'create']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsOwnerOrAdmin]

        return [permission() for permission in permission_classes]

