from rest_framework import serializers

from courses.models.review import Review

class ReviewSerializer(serializers.SerializerMethodField):
    user = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'rating', 'comment', 'created_at']
