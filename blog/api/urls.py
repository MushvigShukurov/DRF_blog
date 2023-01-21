from django.urls import path
from blog.api.views import BlogListCreateAPIView, UserListCreateAPIView, BlogDetailAPIView, UserDetailAPIView, CommentCreateAPIView, CommentsAPIView,  CommentDetailAPIView
urlpatterns = [
    path('blogs/',BlogListCreateAPIView.as_view(),name="blogs"),
    path('blogs/<int:pk>',BlogDetailAPIView.as_view(),name="blog-detail"),
    # path('blogs/<int:pk>/add-comment/', CommentDetailAPIView.as_view(),name="add-comment"),
    path('blogs/<int:pk>/add-comment/', CommentCreateAPIView.as_view(),name="add-comment"),
    path('users/',UserListCreateAPIView.as_view(),name="users"),
    path('users/<int:pk>',UserDetailAPIView.as_view(),name="user-detail"),
    path('comments/',CommentsAPIView.as_view(),name="comments"),
    path('comments/detail/<int:pk>',CommentDetailAPIView.as_view(),name="comment-detail"),
]