from django.db import models
from django.urls import reverse

from user_management.models import Profile


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile, null=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name="article",
    )
    entry = models.TextField()
    createdOn = models.DateTimeField(auto_now_add=True, null=True)
    updatedOn = models.DateTimeField(auto_now=True, null=True)
    imgHeader = models.ImageField(upload_to="images/", null=True)
    category = models.ForeignKey(
        "ArticleCategory", on_delete=models.SET_NULL, related_name="articles", null=True
    )

    def __str__(self):
        return "{} (last updated: {})".format(self.title, self.updatedOn)

    def get_absolute_url(self):
        return reverse("blog:Article", args=[self.pk])

    class Meta:
        ordering = ["-createdOn"]
        unique_together = [
            ["title", "createdOn"],
            ["title", "entry"],
            ["author", "title"]
        ]
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Comment(models.Model):
    author = models.ForeignKey(
        Profile, null=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name="authoredComment"
    )
    article = models.ForeignKey(
        Article, on_delete= models.CASCADE,
        related_name="comment"
    )
    entry = models.TextField()
    createdOn = models.DateTimeField(auto_now_add=True, null=True)
    updatedOn = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return " comment by {} on {}".format(self.author, self.createdOn)
    
    class Meta:
        ordering = ["-createdOn"]
        unique_together = [
            ["entry", "createdOn"],
        ]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class Gallery(models.Model):
    image = models.ImageField(upload_to="images/", null=True)
    article = models.ForeignKey(
        Article, on_delete= models.CASCADE,
        related_name="image"
    )
    def get_absolute_url(self):
        return reverse("blog:add_gallery", args=[self.article.pk])