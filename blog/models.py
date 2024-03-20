from django.db import models
from django.urls import reverse


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Article(models.Model):
    title = models.CharField(max_length=255)
    entry = models.TextField()
    createdOn = models.DateTimeField(auto_now_add=True, null=True)
    updatedOn = models.DateTimeField(auto_now=True, null=True)
    
    category = models.ForeignKey(
        'ArticleCategory',
        on_delete=models.CASCADE,
        related_name='articles'
    )

    def __str__(self):
        return '{} (last updated: {})'.format(self.title, self.updatedOn)
    
    def get_absolute_url(self):
        return reverse('blog:Article', args=[self.pk])
    
    class Meta:
        ordering = ['-createdOn']
        unique_together = [['title','createdOn'],['title','entry'],]
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'