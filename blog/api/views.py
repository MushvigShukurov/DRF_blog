from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from blog.api.serializers import BlogSerializer, UserSerializer, RaitingSerializer, CommentSerializer
from blog.models import Blog, Comment, BlogRaiting
from django.contrib.auth.models import User
from rest_framework import permissions
from blog.api.permissions import IsAdminUserOrReadOnly


class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [IsAdminUserOrReadOnly]
    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)
        

class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)



class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    def perform_create(self, serializer):
        blog_pk = self.kwargs.get("pk")
        blog = get_object_or_404(Blog,pk=blog_pk)
        serializer.save(blog=blog)

class CommentDetailAPIView(DestroyModelMixin,generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class CommentsAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer  



