from django.contrib.auth import get_user_model
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

class UserSerializer(serializers.ModelSerializer):
    """User serializer"""
    class Meta:
        model = get_user_model()
        fields = ("id", "username",)
