from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.ProfileDetailView.as_view()),
    # path('<int:pk>/update/', views.UpdateProfileView.as_view())
]

