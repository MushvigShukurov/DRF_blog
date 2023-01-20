from rest_framework import serializers
from blog.models import Blog
from datetime import datetime
from django.utils.timesince import timesince
from django.utils import timezone
from django.contrib.auth.models import User
# Model Serializer

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User 
#         fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    gun_evvel = serializers.SerializerMethodField()
    # author = serializers.StringRelatedField()
    # author = UserSerializer()
    # author = UserSerializer(read_only=True)
    class Meta:
        model = Blog 
        fields = "__all__"
        # fields = ['title']
        # exclude = ['title']
        # read_only_fields = ['id','title']
    def get_gun_evvel(self,object):
        now = timezone.now()
        cr_at = object.created_at
        gunler = timesince(cr_at,now)
        return gunler + " ago"



# class BlogSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()

#     title = serializers.CharField()
#     description = serializers.CharField()
#     content = serializers.CharField()
#     slug = serializers.SlugField(read_only=True)
#     is_delete = serializers.BooleanField()

#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)



#     def create(self, validated_data):
#         return Blog.objects.create(**validated_data)


#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author',instance.author)
#         instance.title = validated_data.get('title',instance.title)
#         instance.description = validated_data.get('description',instance.description)
#         instance.content = validated_data.get('content',instance.content)
#         instance.slug = validated_data.get('slug',instance.slug)
#         instance.is_delete = validated_data.get('is_delete',instance.is_delete)
#         instance.save()
#         return instance

#     def validate(self,data): # object Level
#         if len(data['title']) <10:
#             raise serializers.ValidationError(
#                 "Title minimum 10 xarakterden ibaret olmalidir."
#             )
#         return data

#     # def validate_slug(self, value):
#     #     has_slug = Blog.objects.filter(slug=value).count()
#     #     print(value)
#     #     print("HAS SLUG :",has_slug)
#     #     if has_slug > 0:
#     #         raise serializers.ValidationError(
#     #             "Slug fields are unique!"
#     #         )
#     #     return value





class UserSerializer(serializers.ModelSerializer):
    # blogs = serializers.SerializerMethodField()
    bloqlar = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='blog-detail'
    )
    class Meta:
        model = User 
        fields = "__all__"

    # def get_blogs(self,object):
    #     # print(object)
    #     blogs = Blog.objects.filter(author=object.id)
    #     blogs = BlogSerializer(blogs,many=True)
    #     return blogs.data