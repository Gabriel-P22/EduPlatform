from rest_framework import serializers

from courses.models.module import Module
from .lessonSerializer import LessonSerializer

class ModuleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['id', 'title', 'created_at', 'lessons']