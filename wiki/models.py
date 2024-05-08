from datetime import datetime

from django.db import models
from django.urls import reverse

from user_management.models import Profile

# Create your models here.


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    description = models.TextField()

    class Meta:
        ordering = ["name"]


class Article(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    author = models.ForeignKey(
        Profile,
        default=None,
        null=True,
        on_delete=models.SET_NULL,
        related_name="profiles",
    )

    category = models.ForeignKey(
        ArticleCategory,
        default=None,
        null=True,
        on_delete=models.SET_NULL,
        related_name="articles",
    )

    header = models.ImageField(upload_to="images/", null=True)

    entry = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def get_absolute_url(self):
        return reverse("wiki:article-detail", args=[self.pk])

    class Meta:
        ordering = ["-created_on"]


class Comment(models.Model):
    author = models.ForeignKey(
        Profile,
        default=None,
        null=True,
        on_delete=models.SET_NULL,
        related_name="users",
    )

    article = models.ForeignKey(
        Article,
        default=None,
        null=True,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    entry = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ["created_on"]
