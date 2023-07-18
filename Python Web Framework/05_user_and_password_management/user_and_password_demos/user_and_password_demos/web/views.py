from django.shortcuts import render
from django.views import generic as web_views
# Create your views here.

class IndexView(web_views.TemplateView):
    template_name = 'web/index.html'

