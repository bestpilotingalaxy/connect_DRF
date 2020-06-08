from django.urls import path
from . import views

urlpatterns = [
    path("adverts/", views.AdvertListView.as_view()),
    path("advert/<int:pk>/", views.AdvertDetailView.as_view()),
    path("review/", views.ReviewCreateView.as_view()),

]
