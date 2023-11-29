from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "index.html"

class AboutUs(TemplateView):
    template_name = "pages/about_us.html"