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
from blog.api.permissions import IsAdminUserOrReadOnly, IsOwnerOfCommentOrReadOnly
from rest_framework.exceptions import ValidationError
from blog.api.pagination import OurPagination

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
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)



class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = OurPagination




class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]




class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        blog_pk = self.kwargs.get("pk")
        blog = get_object_or_404(Blog,pk=blog_pk)
        author_pk = self.request.user.id 
        author = get_object_or_404(User,pk=author_pk)
        comments = Comment.objects.filter(blog=blog,author=author)
        if comments.exists():
            raise ValidationError("Comment yazmisan da bro")
        serializer.save(blog=blog,author=author)

class CommentDetailAPIView(DestroyModelMixin,generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 
    permission_classes = [IsOwnerOfCommentOrReadOnly]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class CommentsAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer  



class BlogRaitingCreate(generics.CreateAPIView):
    queryset = BlogRaiting.objects.all()
    serializer_class = RaitingSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        blog_pk = self.kwargs.get("pk")
        blog = get_object_or_404(Blog,pk=blog_pk)
        user_pk = self.request.user.id 
        user = get_object_or_404(User,pk=user_pk)
        raitings = BlogRaiting.objects.filter(blog=blog,user=user)
        if raitings.exists():
            raise ValidationError("Brooo Puan vermisen de ))")
        serializer.save(blog=blog,user=user)
