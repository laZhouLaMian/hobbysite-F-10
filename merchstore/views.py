from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import ProductType, Product


class ProductListView(ListView):
    model = ProductType
    template_name = "merchstore_product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "merchstore_product_detail.html"
