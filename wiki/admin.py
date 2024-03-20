from django.contrib import admin

from .models import Article, ArticleCategory


class ArtCategAdmin(admin.ModelAdmin):
    model = ArticleCategory


class ArticleAdmin(admin.ModelAdmin):
    model = Article


admin.site.register(ArticleCategory, ArtCategAdmin)
admin.site.register(Article, ArticleAdmin)
