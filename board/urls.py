from django.urls import path
from rest_framework.routers import format_suffix_patterns

from . import views

urlpatterns = format_suffix_patterns([
    path('advert/<int:pk>/', views.AdvertViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),
    path('advert/', views.AdvertViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    )),
    path('review/<int:pk>/', views.ReviewViewSet.as_view(
        {'put': 'update', 'delete': 'destroy'}
    )),
    path('review/', views.ReviewViewSet.as_view(
        {'post': 'create'}
    )),
])


