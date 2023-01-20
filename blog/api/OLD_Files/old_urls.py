from django.urls import path
from blog.api.OLD_Files.old_views import blog_list_create_api_view, blog_detail, BlogListCreateApiView, BlogDetail, UserListCreateApiView, BlogListCreateAPIView
urlpatterns = [

    # Generic Api View + Mixins
    path('blogs/',BlogListCreateAPIView.as_view(),name="blogs"),


    # path('blogs/',BlogListCreateApiView.as_view(),name="blogs"),
    # path('users/',UserListCreateApiView.as_view(),name="users"),
    # path('blogs/<int:pk>',BlogDetail.as_view(),name="blog-detail"),

    # Function Based Urls
    # path('blogs/',blog_list_create_api_view,name="blogs"),
    # path('blogs/<int:pk>',blog_detail,name="blog-detail"),
]