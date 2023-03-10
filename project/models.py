from django.db import models
from django.utils import timezone

# Create your models here.

CATEGORY_LIST = (
    ("web_dev","Web Development"),
    ("cyber","Cyber Security"),
    ("automation","Automation"),
)

# Create projects
class Project(models.Model):
    title = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_projects')
    description = models.TextField(max_length=2000)
    category = models.CharField(max_length=20, choices=CATEGORY_LIST)
    views = models.IntegerField(default=0)
    date_create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# Create type projects
class Topic(models.Model):
    project = models.ForeignKey("Project", related_name="topic", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.project.title + " - " + self.title

# Create users