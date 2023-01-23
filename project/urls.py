from django.urls import path, include
from .views import homepage, homeprojects

urlpatterns = [
    path('', homepage),
    path('projects/', homeprojects),
]