from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class NotFoundView(TemplateView):
    template_name = "404.html"


class ServerErrorView(TemplateView):
    template_name = "500.html"
