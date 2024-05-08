from django.db import models
from django.urls import reverse

from user_management.models import Profile


OPEN = "0"
FULL = "1"
COMPLETED = "2"
DISCONTINUED = "3"


class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    STATUS_CHOICES = {
        OPEN: "Open",
        FULL: "Full",
        COMPLETED: "Completed",
        DISCONTINUED: "Discontinued",
    }
    author = models.ForeignKey(to=Profile, on_delete=models.CASCADE, related_name="commission")
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="open")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        return reverse("commissions:detail", args=[str(self.pk)])


class Comment(models.Model):
    commission = models.ForeignKey(
        Commission, on_delete=models.CASCADE, related_name="comments"
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
