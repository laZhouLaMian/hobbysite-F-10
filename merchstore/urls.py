from django.urls import path

from .views import *

urlpatterns = [
    path("items", ProductListView.as_view(), name="merchstore_product_list"),
    path(
        "item/<int:pk>", ProductDetailView.as_view(), name="merchstore_product_detail"
    ),
    path("item/add", ProductCreateView.as_view(),
         name="merchstore_product_create"),
    path("item/<int:pk>/edit", ProductUpdateView.as_view(),
         name="merchstore_product_update"),
    path("cart", CartView.as_view(), name="merchstore_cart"),
    path("transactions", TransactionListView.as_view(),
         name="merchstore_transaction_list")
]

app_name = "merchstore"
