from django.urls import path

from .views import ProfileCreateView, ProfileUpdateView


urlpatterns = [
    path("<int:pk>", ProfileUpdateView.as_view(), name="profile_update"),
    path("create", ProfileCreateView.as_view(), name="profile_create"),
]

app_name = "user_management"
