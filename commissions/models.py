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


class Job(models.Model):
    STATUS_CHOICES = {
        OPEN: "Open",
        FULL: "Full",
    }
        
    commission = models.ForeignKey(
        Commission, on_delete=models.CASCADE, related_name="job"
    )
    role = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default=STATUS_CHOICES[OPEN], choices=STATUS_CHOICES)
    manpower_required = models.IntegerField()

    class Meta:
        ordering = ["status", "-manpower_required", "role"]

    def __str__(self):
        return str(self.role)

    class Meta:
        ordering = ["-created_on"]
