from django.db import models


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
        on_delete=models.CASCADE,
        related_name="products"
    )
    description = models.TextField()
    price = models.DecimalField(decimal_places=2)

    class Meta:
        ordering = ["name"]
