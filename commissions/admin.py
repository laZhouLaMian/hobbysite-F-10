from django.contrib import admin

from .models import Comment, Commission


class CommentAdmin(admin.TabularInline):
    model = Comment


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    inlines = [CommentAdmin]


admin.site.register(Commission, CommissionAdmin)
