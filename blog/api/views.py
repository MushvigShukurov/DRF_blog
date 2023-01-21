from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from blog.api.serializers import BlogSerializer, UserSerializer, RaitingSerializer, CommentSerializer
from blog.models import Blog, Comment, BlogRaiting
from django.contrib.auth.models import User 



class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

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





# class CommentListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

# class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

# Generic Api Views :
"""
class BlogListCreateAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request,*args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request,*args, **kwargs)

class UserListCreateAPIView(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request,*args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request,*args, **kwargs)
"""