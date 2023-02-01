from .models import Project

def list_projects_recent(request):
    list_projects = Project.objects.all().order_by('-date_create')[0:10]
    return {"list_projects_recent":list_projects}

def list_projects_top(request):
    list_projects = Project.objects.all().order_by('-views')[0:10]
    return {"list_projects_top":list_projects}