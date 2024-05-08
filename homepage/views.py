from django.views.generic.base import TemplateView


class HomepageView(TemplateView):
    template_name = "homepage.html"
