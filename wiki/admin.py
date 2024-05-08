from django.contrib import admin

from .models import Article, ArticleCategory, Comment


class ArtCategAdmin(admin.ModelAdmin):
    model = ArticleCategory


class ArticleAdmin(admin.ModelAdmin):
    model = Article


class TestAdmin(admin.ModelAdmin):
    model = Comment


admin.site.register(ArticleCategory, ArtCategAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, TestAdmin)
