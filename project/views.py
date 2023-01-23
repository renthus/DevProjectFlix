from django.shortcuts import render
from .models import Project
from django.views.generic import TemplateView, ListView

# Create your views here.

# def homepage(request):
#     return render(request, "homepage.html")

class Homepage(TemplateView):
    template_name = "homepage.html"

# def homeprojects(request):
#     context = {}
#     project_list = Project.objects.all()
#     context['projects_list'] = project_list
#     return render(request, "homeprojects.html", context)

class Homeprojects(ListView):
    template_name = "homeprojects.html"
    model = Project