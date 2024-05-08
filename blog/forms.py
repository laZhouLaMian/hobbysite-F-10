from django import forms

from .models import Article, Comment, Gallery


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "entry", "imgHeader", "category",]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["entry",]

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = "__all__"