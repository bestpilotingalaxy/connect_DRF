from django.urls import path
from . import views

urlpatterns = [
    path("adverts/", views.AdvertListView.as_view()),
    # path("advert/<int:pk>/delete", views.AdvertDeleteView.as_view()),
    path("advert/<int:pk>/update", views.AdvertUpdateView.as_view()),
    path("advert/<int:pk>/", views.AdvertDetailView.as_view()),
    path("review/", views.ReviewCreateView.as_view()),
]
