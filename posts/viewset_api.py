from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PostSerializer
from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]