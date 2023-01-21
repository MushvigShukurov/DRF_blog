from django.urls import path
from blog.api.views import BlogListCreateAPIView, UserListCreateAPIView
urlpatterns = [
    path('blogs/',BlogListCreateAPIView.as_view(),name="blogs"),
    # path('blogs/<int:pk>',BlogDetail.as_view(),name="blog-detail"),
    path('users/',UserListCreateAPIView.as_view(),name="users"),
]