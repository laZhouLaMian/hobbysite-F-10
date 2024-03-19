from datetime import datetime

from django.db import models
from django.urls import reverse

# Create your models here.


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Article(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.SET_NULL,
        related_name="articles",
        default=1,
        null=True,
    )
    entry = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def get_absolute_url(self):
        return reverse("wiki:article-detail", args=[self.pk])

    class Meta:
        ordering = ["-created_on"]
