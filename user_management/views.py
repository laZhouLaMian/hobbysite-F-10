from django.views.generic.edit import UpdateView, CreateView
from .models import Profile


class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ["display_name", "email"]
    template_name = "profile_update.html"


class ProfileCreateView(CreateView):
    model = Profile
    template_name = "profile_create.html"
