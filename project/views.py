from django.shortcuts import render
from .models import Project
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

class Homepage(TemplateView):
    template_name = "homepage.html"

class Homeprojects(ListView):
    template_name = "homeprojects.html"
    model = Project

class DetailsProject(DetailView):
    template_name = "detailsproject.html" 
    model = Project

# def homepage(request):
#     return render(request, "homepage.html")

# def homeprojects(request):
#     context = {}
#     project_list = Project.objects.all()
#     context['projects_list'] = project_list
#     return render(request, "homeprojects.html", context)