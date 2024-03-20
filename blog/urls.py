from django.urls import path

from .views import ArticleDetailView, CategoryListView

urlpatterns = [
    path("articles/", CategoryListView.as_view(), name="ArticleCategory"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="Article"),
]

app_name = "blog"
