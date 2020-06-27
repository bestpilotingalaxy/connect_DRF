
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView,
    DestroyAPIView
)

from .serializers import (
    AdvertSerializer, AdvertDetailSerializer, ReviewCreateSerializer,
    AdvertCreateSerializer
)
from .models import Advert
from .service import AdvertFilter


class AdvertListView(ListAPIView):
    """Serialize queryset of adverts and return"""
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    # Filter queryset by some fields
    filterset_class = AdvertFilter


class AdvertDetailView(RetrieveAPIView):
    """Serialize single advert object and return detail data"""
    queryset = Advert.objects.all()
    serializer_class = AdvertDetailSerializer


class AdvertUpdateView(UpdateAPIView):
    """Update advert"""
    serializer_class = AdvertDetailSerializer


class AdvertCreateView(CreateAPIView):
    """Create Advert object"""
    serializer_class = AdvertCreateSerializer


class AdvertDeleteView(DestroyAPIView):
    queryset = Advert.objects.filter()


class ReviewCreateView(CreateAPIView):
    """Get POST data and create review"""
    serializer_class = ReviewCreateSerializer
