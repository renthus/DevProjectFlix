from django.urls import path, include
from .views import Homepage, Homeprojects, DetailsProject


urlpatterns = [
    path('', Homepage.as_view()),
    path('projects/', Homeprojects.as_view()),
    path('projects/<int:pk>', DetailsProject.as_view()),
]