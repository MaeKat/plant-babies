from django.urls import path
from .views import StoryMapView, HomePageView


urlpatterns = [
    path('story-map',StoryMapView.as_view(),name ='story-map'),
    path('home',HomePageView.as_view(),name = 'homepage'),

]
