from django.db import models
from accounts.models.user.user import User
from .lesson import Lesson


class WatchedLesson(models.Model):
    user = models.ForeignKey(User, related_name='watched_lessons', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name='watched_by', on_delete=models.CASCADE)
    watched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'courses_watched_lesson'
        unique_together = ('user', 'lesson')