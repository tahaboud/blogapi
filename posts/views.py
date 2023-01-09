from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """Post list create api view"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """Post retrieve, update and delete api view"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer