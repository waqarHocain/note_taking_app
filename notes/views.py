from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = "notes/home.html"
