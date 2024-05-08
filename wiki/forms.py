from django import forms

from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "title",
            "category",
            "entry",
            "header",
        ]


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "entry",
        ]
