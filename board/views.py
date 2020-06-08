from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    AdvertSerializer, AdvertDetailSerializer, ReviewCreateSerializer
)
from .models import Advert


class AdvertListView(APIView):
    """Serialize queryset of adverts and return"""
    def get(self, request):
        adverts = Advert.objects.all()
        serializer = AdvertSerializer(adverts, many=True)

        return Response(serializer.data)


class AdvertDetailView(APIView):
    """Serialize single advert object and return detail data"""
    def get(self, request, pk):
        advert = Advert.objects.get(pk=pk)
        serializer = AdvertDetailSerializer(advert)

        return Response(serializer.data)


class ReviewCreateView(APIView):
    """Get POST data and create review"""
    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()

        return Response(status=201)
