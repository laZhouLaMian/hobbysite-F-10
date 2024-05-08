from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic.edit import UpdateView

from user_management.models import Profile

from .forms import ArticleCommentForm, ArticleForm
from .models import Article, ArticleCategory, Comment


def ArticleListView(request):
    articles = Article.objects.all()

    if request.user.is_authenticated:
        user_articles = Article.objects.filter(author__user=request.user)
    else:
        user_articles = None

    categories = ArticleCategory.objects.all()

    ctx = {
        "articles": articles,
        "user_articles": user_articles,
        "categories": categories,
    }

    return render(request, "wiki_article_list.html", ctx)


def ArticleDetailView(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleCommentForm()

    if request.method == "POST":
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            cmt = Comment()
            cmt.author = Profile.objects.get(user=request.user)
            cmt.article = article
            cmt.entry = form.cleaned_data.get("entry")
            cmt.save()
            return redirect("wiki:article-detail", pk=article.pk)

    ctx = {"form": form, "article": article}

    return render(request, "wiki_article_detail.html", ctx)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ["title", "category", "entry", "header"]
    template_name = "wiki_article_edit.html"


@login_required
def ArticleCreateView(request):
    form = ArticleForm()

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = Article()
            article.title = form.cleaned_data.get("title")
            article.category = form.cleaned_data.get("category")
            article.author = Profile.objects.get(user=request.user)
            article.header = form.cleaned_data.get("header")
            article.entry = form.cleaned_data.get("entry")
            article.save()
            return redirect("wiki:article-detail", pk=article.pk)

    ctx = {"form": form}

    return render(request, "wiki_article_create.html", ctx)
