from django.urls import path

from .views import ProductDetailView, ProductListView

urlpatterns = [
    path("items", ProductListView.as_view(), name="merchstore_product_list"),
    path(
        "item/<int:pk>", ProductDetailView.as_view(), name="merchstore_product_detail"
    ),
]

app_name = "merchstore"
