from django.contrib import admin

from .models import Article, ArticleCategory


class ArticleInline(admin.TabularInline):
    model = Article

class CategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [ArticleInline,]

    search_fields = ['name',]
    list_display = ['name', 'description',]

class ArticleAdmin(admin.ModelAdmin):
    model = Article

    search_fields = ['title',]
    list_display = ['category', 'title', 'updatedOn']
    list_filter = ['category']

    fieldsets = [
        ('Details', {
            'fields': [
                ('category', 'title'),
                'entry'
            ]
        })
    ]

admin.site.register(ArticleCategory, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)