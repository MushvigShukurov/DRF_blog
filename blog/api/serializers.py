from rest_framework import serializers
from blog.models import Blog, Comment, BlogRaiting
from datetime import datetime
from django.utils.timesince import timesince
from django.utils import timezone
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    # blog = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['blog','author']

class RaitingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogRaiting
        fields = "__all__"
        read_only_fields = ["id","created_at","updated_at","blog","user"]
        

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,read_only=True)
    raitings = RaitingSerializer(many=True,read_only=True)
    class Meta:
        model = Blog 
        fields = "__all__"
        read_only_fields = ['slug','is_delete','author']


class UserSerializer(serializers.ModelSerializer):
    bloqlar = serializers.HyperlinkedRelatedField( many=True, read_only=True, view_name='blog-detail' )
    class Meta:
        model = User 
        fields = "__all__"
        read_only_fields = ['last_login','is_superuser','is_staff','is_active','groups','user_permissions','date_joined']
