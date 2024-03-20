from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Article, ArticleCategory


class ArticleListView(ListView):
    model = ArticleCategory
    template_name = "wiki_article_list.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "wiki_article_detail.html"
