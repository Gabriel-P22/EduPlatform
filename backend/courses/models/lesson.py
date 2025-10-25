from django.db import models
from .module import Module

class Lesson(models.Model):
    module = models.ForeignKey(Module, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    time_estimate = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

