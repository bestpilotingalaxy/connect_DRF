from django_filters import rest_framework as filters

from board.models import Advert


class AdvertFilter(filters.FilterSet):
    """Filter instance for filtering adverts by price"""
    price = filters.RangeFilter()

    class Meta:
        model = Advert
        fields = ('advert_category', 'content_type', 'platform', 'price')