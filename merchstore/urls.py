from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('list', ProductListView.as_view(), name="merchstore_product_list"),
    path('item/<int:pk>', ProductDetailView.as_view(),
         name="merchstore_product_detail")
]

app_name = "merchstore"
