from django.urls import path

from .views import ArticleDetailView, ArticleListView

urlpatterns = [
    path("articles", ArticleListView.as_view(), name="list"),
    path("article/<pk>", ArticleDetailView.as_view(), name="article-detail"),
]

app_name = "tasks"
