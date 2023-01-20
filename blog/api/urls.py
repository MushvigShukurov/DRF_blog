from django.urls import path
from blog.api.views import blog_list_create_api_view, blog_detail, BlogListCreateApiView, BlogDetail, UserListCreateApiView
urlpatterns = [
    path('blogs/',BlogListCreateApiView.as_view(),name="blogs"),
    path('users/',UserListCreateApiView.as_view(),name="users"),
    path('blogs/<int:pk>',BlogDetail.as_view(),name="blog-detail"),

    # Function Based Urls
    # path('blogs/',blog_list_create_api_view,name="blogs"),
    # path('blogs/<int:pk>',blog_detail,name="blog-detail"),
]