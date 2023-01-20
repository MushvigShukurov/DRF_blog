from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Blog, Comment, BlogRaiting
from blog.api.serializers import BlogSerializer, UserSerializer, RaitingSerializer
from django.contrib.auth.models import User 
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin