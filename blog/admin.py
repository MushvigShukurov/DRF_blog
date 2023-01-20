from django.contrib import admin
from blog.models import Blog
# Register your models here.
# admin.site.register(Blog)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']