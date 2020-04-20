from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class StoryMapView(TemplateView):
    template_name = 'story-map.html'

class BaseView(TemplateView):
    template_name = 'base.html'

class HomePageView(TemplateView):
    template_name = 'homepage.html'  
