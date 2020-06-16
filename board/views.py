from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
)

from .serializers import (
    AdvertSerializer, AdvertDetailSerializer, ReviewCreateSerializer
)
from .models import Advert


class AdvertListView(ListAPIView):
    """Serialize queryset of adverts and return"""
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer


class AdvertDetailView(RetrieveAPIView):
    """Serialize single advert object and return detail data"""
    queryset = Advert.objects.filter()
    serializer_class = AdvertDetailSerializer


class AdvertUpdateView(UpdateAPIView):
    """Update"""
    serializer_class = AdvertDetailSerializer


# class AdvertDeleteView(DestroyAPIView):
#
#     queryset = Advert.objects.filter()
#     serializer_class = AdvertDetailSerializer


class ReviewCreateView(CreateAPIView):
    """Get POST data and create review"""
    serializer_class = ReviewCreateSerializer
