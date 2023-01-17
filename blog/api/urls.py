from django.urls import path
from blog.api.views import blog_list_create_api_view
urlpatterns = [
    path('blogs/',blog_list_create_api_view,name="blogs"),
]