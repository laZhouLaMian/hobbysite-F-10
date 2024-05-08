from django.urls import path

from .views import commission_detail, commission_list, commission_create, commission_edit

urlpatterns = [
    path("list", commission_list, name="list"),
    path("detail/<int:pk>", commission_detail, name="detail"),
    path("add", commission_create, name="create"),
    path("<int:pk>/edit", commission_edit, name="edit"),
]

app_name = "commissions"
