from django.db import models
from accounts.models.user.user import User
from .courses import Courses


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, related_name='orders', on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    external_payment_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
