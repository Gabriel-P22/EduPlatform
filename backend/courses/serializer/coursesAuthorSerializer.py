from rest_framework import serializers
from accounts.models import User
from django.db.models import Avg

class CourseAuthorSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    total_courses = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['name', 'email', 'average_rating', 'total_courses']

    def get_average_rating(self, obj):
        return round(obj.courses.aggregate(average_rating=Avg('average_rating'))['average_rating'] or 0)

    def get_total_courses(self, obj):
        return obj.courses.count()
