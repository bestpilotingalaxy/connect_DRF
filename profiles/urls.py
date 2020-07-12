from django.urls import path
from rest_framework.routers import format_suffix_patterns

from . import views

urlpatterns = format_suffix_patterns([
    path('<int:pk>/',
         views.ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update'}),
         name='profile'),
])
