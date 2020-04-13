from django.urls import path
from .views import StoryMapView


urlpatterns = [
    path('story-map',StoryMapView.as_view(),name ='story-map')

]