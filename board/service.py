from django_filters import rest_framework as filters

from board.models import Advert
from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        """Return True if user is object owner or Admin"""
        return obj.user == request.user or request.user.is_staff


class AdvertFilter(filters.FilterSet):
    price = filters.RangeFilter()

    class Meta:
        model = Advert
        fields = ('advert_category', 'content_type', 'platform', 'price')
