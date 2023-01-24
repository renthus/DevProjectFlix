from django.urls import path, include
from .views import Homepage, Homeprojects, Detailsproject

app_name = 'project'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('projects/', Homeprojects.as_view(), name='homeprojects'),
    path('projects/<int:pk>', Detailsproject.as_view(), name='detailsproject'),
]