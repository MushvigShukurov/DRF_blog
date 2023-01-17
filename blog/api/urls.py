from django.urls import path
from blog.api.views import blog_list_create_api_view, blog_detail
urlpatterns = [
    path('blogs/',blog_list_create_api_view,name="blogs"),
    path('blogs/<int:pk>',blog_detail,name="blog-detail"),
]