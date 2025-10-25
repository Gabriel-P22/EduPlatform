from django.db import models

from .tag import Tag
from accounts.models.user.user import User

class Courses(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.TextField()
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='courses')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_reviews = models.PositiveIntegerField(default=0)
    average_rating = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, related_name='courses', on_delete=models.CASCADE)
    level = models.TextField(
        max_length=50,
        choices=[
            ('beginner', 'Iniciante'),
            ('intermediate', 'Intermediário'),
            ('advanced', 'Acançado')
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)