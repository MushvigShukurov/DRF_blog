from rest_framework import serializers
from blog.models import Blog, Comment, BlogRaiting
from datetime import datetime
from django.utils.timesince import timesince
from django.utils import timezone
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class RaitingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogRaiting
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog 
        fields = "__all__"
        read_only_fields = ['slug','is_delete']
class UserSerializer(serializers.ModelSerializer):
    # bloqlar = serializers.HyperlinkedRelatedField( many=True, read_only=True, view_name='blog-detail' )
    class Meta:
        model = User 
        fields = "__all__"
