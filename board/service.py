from django_filters import rest_framework as filters

from board.models import Advert


class AdvertFilter(filters.FilterSet):
    price = filters.RangeFilter()

    class Meta:
        model = Advert
        fields = ('advert_category', 'content_type', 'platform', 'price')
