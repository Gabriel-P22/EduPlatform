from django.db import models
from .courses import Courses

class Module(models.Model):
    courses = models.ForeignKey(Courses, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

