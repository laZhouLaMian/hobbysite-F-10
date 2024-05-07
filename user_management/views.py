from django.views.generic.edit import UpdateView, CreateView
from .models import Profile


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = "profile_update.html"


class ProfileUpdateView(CreateView):
    model = Profile
    template_name = "profile_create.html"
