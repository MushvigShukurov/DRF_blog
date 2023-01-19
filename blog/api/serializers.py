from rest_framework import serializers
from blog.models import Blog
class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()

    title = serializers.CharField()
    description = serializers.CharField()
    content = serializers.CharField()
    slug = serializers.SlugField(read_only=True)
    is_delete = serializers.BooleanField()

    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)



    def create(self, validated_data):
        return Blog.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.author = validated_data.get('author',instance.author)
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.content = validated_data.get('content',instance.content)
        instance.slug = validated_data.get('slug',instance.slug)
        instance.is_delete = validated_data.get('is_delete',instance.is_delete)
        instance.save()
        return instance

    def validate(self,data): # object Level
        if len(data['title']) <10:
            raise serializers.ValidationError(
                "Title minimum 10 xarakterden ibaret olmalidir."
            )
        return data

    # def validate_slug(self, value):
    #     has_slug = Blog.objects.filter(slug=value).count()
    #     print(value)
    #     print("HAS SLUG :",has_slug)
    #     if has_slug > 0:
    #         raise serializers.ValidationError(
    #             "Slug fields are unique!"
    #         )
    #     return value