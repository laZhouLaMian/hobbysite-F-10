from django.http import HttpResponseRedirect
from django.urls import is_valid_path
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, ProductType, Transaction
from .forms import ProductForm, TransactionForm


class ProductListView(ListView):
    model = ProductType
    template_name = "merchstore_product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "merchstore_product_detail.html"

    form = TransactionForm()

    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = "/registration/login"
    model = Product
    template_name = "merchstore_product_create.html"

    fields = ["name", "productType", "description", "price", "stock", "status"]

    form = ProductForm()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = self.form
        return ctx

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)
        if form.is_valid():
            product = Product()
            product.name = form.cleaned_data.get("name")
            product.productType = form.cleaned_data.get("productType")
            product.description = form.cleaned_data.get("description")
            product.price = form.cleaned_data.get("price")
            product.stock = form.cleaned_data.get("stock")
            product.status = form.cleaned_data.get("status")
            product.owner = request.user.profile
            product.save()
            return HttpResponseRedirect("/merchstore/items")
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "merchstore_product_update.html"

    fields = ["name", "productType", "description", "price", "stock", "status"]


class CartView(ListView):
    model = Product
    template_name = "merchstore_cart.html"


class TransactionListView(ListView):
    model = Transaction
    template_name = "merchstore_transaction_list.html"
