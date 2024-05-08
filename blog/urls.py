from django.urls import path

from .views import CategoryListView, ArticleUpdateView, GalleryCreateView
from .views import ArticleDetailView, ArticleCreateView

urlpatterns = [
    path("articles/", CategoryListView.as_view(), name="ArticleCategory"),
    path("article/<int:pk>", ArticleDetailView, name="Article"),
    path("article/add", ArticleCreateView, name="ArticleCreate"),
    path("article/<int:pk>/edit", ArticleUpdateView.as_view(), name="ArticleUpdate"),
    path("articles/<int:pk>/add_gallery", GalleryCreateView.as_view(), name="Gallery")
]

app_name = "blog"