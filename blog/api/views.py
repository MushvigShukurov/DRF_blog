from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from blog.api.serializers import BlogSerializer, UserSerializer, RaitingSerializer
from blog.models import Blog, Comment, BlogRaiting
from django.contrib.auth.models import User 



class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer






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