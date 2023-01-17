from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Blog
from blog.api.serializers import BlogSerializer 
from django.shortcuts import redirect

@api_view(['GET','POST'])
def blog_list_create_api_view(request):
    if request.method == "GET":
        blogs = Blog.objects.filter(is_delete=False)
        serializer = BlogSerializer(blogs,many=True)      
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("blogs")
            # return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def blog_detail(request,pk):
    try:
        blog = Blog.objects.get(pk=pk)        
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = BlogSerializer(blog)
        return Response(serializer.data) 
    elif request.method == "PUT":
        serializer = BlogSerializer(blog,data=request.data)
        if serializer.is_valid(): serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK) 
    elif request.method == "DELETE":
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)