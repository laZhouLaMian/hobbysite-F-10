from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "productType",
                  "description", "price", "stock", "status"]


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["amount"]
