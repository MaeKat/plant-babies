from django.urls import path
from .views import StoryMapView, BaseView, HomePageView


urlpatterns = [
    path('story-map',StoryMapView.as_view(),name ='story-map'),
    path('base',BaseView.as_view(),name ='base'),
    path('home',HomePageView.as_view(),name = 'homepage'),

]
