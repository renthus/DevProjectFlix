from django.urls import path, include
from .views import Homepage, Homeprojects


urlpatterns = [
    path('', Homepage.as_view()),
    path('projects/', Homeprojects.as_view()),
]