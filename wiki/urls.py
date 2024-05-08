from django.urls import path

from .views import (
    ArticleCreateView,
    ArticleDetailView,
    ArticleListView,
    ArticleUpdateView,
)

urlpatterns = [
    path("articles", ArticleListView, name="list"),
    path("article/<int:pk>", ArticleDetailView, name="article-detail"),
    path("article/add", ArticleCreateView, name="article-add"),
    path("article/<int:pk>/edit", ArticleUpdateView.as_view(), name="article-update"),
]

app_name = "tasks"
