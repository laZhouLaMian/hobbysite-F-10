from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy

from .models import Article, ArticleCategory, Comment, Gallery
from .forms import ArticleForm, CommentForm, GalleryForm
from user_management.models import Profile


class CategoryListView(ListView):
    model = ArticleCategory
    template_name = "blog_category.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["authoredArticles"] = Article.objects.filter(author__user=self.request.user.id)
        ctx["excludedArticles"] = Article.objects.exclude(author__user=self.request.user.id)
        ctx["form"] = ArticleForm()
        return ctx


def ArticleDetailView(request, pk):
    article = Article.objects.get(pk=pk)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = Comment()
            comment.author = Profile.objects.get(user=request.user)
            comment.entry = form.cleaned_data.get("entry")
            comment.article = Article.objects.get(pk=pk)
            comment.save()
            return redirect("blog:Article", pk=pk)

    ctx = {
        "object": article, 
        "form": form,
        "allArticles": Article.objects.all(),
        "comments": Comment.objects.all()
    }
    return render(request, "blog_article.html", ctx)


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
            article.imgHeader = form.cleaned_data.get("imgHeader")
            article.entry = form.cleaned_data.get("entry")
            article.save()
            return redirect("blog:Article", pk=article.pk)

    ctx = {"form": form}
    return render(request, "blog_articleCreate.html", ctx)


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ["title", "category", "entry", "imgHeader", ]
    template_name = "blog_articleUpdate.html"

    def get_success_url(self):
        return reverse_lazy("blog:Article", kwargs={
            "pk": self.object.article.pk
        })


class GalleryCreateView(LoginRequiredMixin, CreateView):
    model = Gallery
    form_class = GalleryForm
    template_name = "blog_addGallery.html"

    def get_success_url(self):
        return reverse_lazy("blog:Article", kwargs={
            "pk": self.object.article.pk
        })