from rest_framework import serializers

from courses.models.lesson import Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'id',
            'title',
            'description',
            'video_url',
            'time_estimate',
            'created_at'
        ]