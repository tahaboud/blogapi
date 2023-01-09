from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """Post serializer"""
    class Meta:
        """Post serializer Meta class"""
        fields = (
        "id",
        "author",
        "title",
        "body",
        "created_at",
        )
        model = Post
