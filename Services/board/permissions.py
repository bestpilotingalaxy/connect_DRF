from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        """Return True if user is object owner or Admin"""
        return obj.user == request.user or request.user.is_staff

