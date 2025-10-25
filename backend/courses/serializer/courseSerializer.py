from rest_framework import serializers

from courses.models.courses import Courses
from .tagSerializer import TagSerializer
from .coursesAuthorSerializer import CourseAuthorSerializer

class CourseSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    author = CourseAuthorSerializer(read_only=True)
    total_enrollments = serializers.SerializerMethodField()

    class Meta:
        model = Courses
        fields = '__all__'

    def get_total_enrollments(self, obj):
        return obj.enrollments.count()
