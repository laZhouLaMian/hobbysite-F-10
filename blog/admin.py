from django.contrib import admin

from .models import Article, ArticleCategory, Comment, Gallery


class ArticleInline(admin.TabularInline):
    model = Article


class CategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [
        ArticleInline,
    ]

    search_fields = [
        "name",
    ]
    list_display = [
        "name",
        "description",
    ]


class GalleryInline(admin.TabularInline):
    model = Gallery

class CommentInline(admin.TabularInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    inline = [CommentInline, GalleryInline]

    search_fields = [
        "title",
    ]
    list_display = ["category", "title", "updatedOn"]
    list_filter = ["category"]

    fieldsets = [("Details", {"fields": [("category", "title"), "entry"]})]

class GalleryAdmin(admin.ModelAdmin):
    model = Gallery

class CommentAdmin(admin.ModelAdmin):
    model = Comment

    list_display = ["article", "author"]

admin.site.register(ArticleCategory, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Comment, CommentAdmin)
