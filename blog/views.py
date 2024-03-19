from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Article


class CategoryListView(ListView):
    model = Article
    template_name = 'category.html'
    
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'