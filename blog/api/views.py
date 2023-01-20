from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Blog
from blog.api.serializers import BlogSerializer, UserSerializer
from django.shortcuts import redirect
from  django.contrib.auth.models import User 

# Class Based View
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

# For User
class UserListCreateApiView(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True,context={'request': request})      
        return Response(serializer.data)
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("users")
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# End For User


class BlogListCreateApiView(APIView):
    def get(self,request):
        blogs = Blog.objects.filter(is_delete=False)
        serializer = BlogSerializer(blogs,many=True)      
        return Response(serializer.data)
    def post(self,request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("blogs")
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class BlogDetail(APIView):
    def get_object_custom(self,pk):
        blog = get_object_or_404(Blog,pk=pk)
        return blog
    def get(self,request,pk):
        blog = self.get_object_custom(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    def put(self,request,pk):
        blog = self.get_object_custom(pk)
        serializer = BlogSerializer(blog,data=request.data)
        if serializer.is_valid(): serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK) 
    def delete(self,request,pk):
        blog = self.get_object_custom(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ----------------


# Function Based Views
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
        # return Response(serializer.errors,serializer.data,status=status.HTTP_200_OK) 
    elif request.method == "DELETE":
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)