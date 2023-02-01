from django.shortcuts import render
from .models import Project
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

class Homepage(TemplateView):
    template_name = "homepage.html"

class Homeprojects(ListView):
    template_name = "homeprojects.html"
    model = Project

class Detailsproject(DetailView):
    template_name = "detailsproject.html" 
    model = Project

    def get(self, request, *args, **kwargs):
        project = self.get_object()
        project.views += 1
        project.save()
        return super(Detailsproject, self).get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(Detailsproject, self).get_context_data(**kwargs)
        projects_relations = Project.objects.filter(category=self.get_object().category)
        context["projects_relations"] = projects_relations
        return context

# def homepage(request):
#     return render(request, "homepage.html")

# def homeprojects(request):
#     context = {}
#     project_list = Project.objects.all()
#     context['projects_list'] = project_list
#     return render(request, "homeprojects.html", context)