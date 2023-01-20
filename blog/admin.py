from django.contrib import admin
from blog.models import Blog, Comment, BlogRaiting
# Register your models here.
# admin.site.register(Blog)
admin.site.register(BlogRaiting)
admin.site.register(Comment)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']