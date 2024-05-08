from django.db import models
from django.urls import reverse

from user_management.models import Profile


class ProductType(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Product(models.Model):

    name = models.CharField(max_length=255)
    productType = models.ForeignKey(
        "ProductType",
        on_delete=models.SET_NULL,
        related_name="products",
        null=True
    )
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()

    class ProductStatus(models.TextChoices):
        AVAILABLE = "AV", "Available"
        ON_SALE = "ON", "On Sale"
        OUT_OF_STOCK = "OU", "Out of Stock"

    status = models.CharField(
        choices=ProductStatus.choices,
        default=ProductStatus.AVAILABLE,
        max_length=15
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("merchstore:merchstore_product_detail", args=[self.pk])

    class Meta:
        ordering = ["name"]


class Transaction(models.Model):
    buyer = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True
    )
    product = models.ForeignKey(
        "Product",
        on_delete=models.SET_NULL,
        null=True
    )
    amount = models.IntegerField()

    class TransactionStatus(models.TextChoices):
        ON_CART = "OC", "On Cart"
        TO_PAY = "TP", "To Pay"
        TO_SHIP = "TS", "To Ship"
        TO_RECEIVE = "TR", "To Receive"
        DELIVERED = "DE", "Delivered"

    status = models.CharField(
        choices=TransactionStatus.choices,
        max_length=15
    )
    createdOn = models.DateTimeField(auto_now_add=True)
