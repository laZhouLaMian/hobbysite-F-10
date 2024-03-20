from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Article, ArticleCategory


class CategoryListView(ListView):
    model = ArticleCategory
    template_name = "category.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article.html"
