from django.urls import path
from . import views

urlpatterns = [
    path("adverts/", views.AdvertListView.as_view()),
    # path("advert/<int:pk>/delete", views.AdvertDeleteView.as_view()),
    path("create/", views.AdvertCreateView.as_view()),
    path("<int:pk>/update/", views.AdvertUpdateView.as_view()),
    path("<int:pk>/review/", views.ReviewCreateView.as_view()),
    path("review/<int:pk>/delete/", views.ReviewDeleteView.as_view()),
    path("<int:pk>/", views.AdvertDetailView.as_view()),
]
