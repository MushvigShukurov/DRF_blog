from django.db import models
from slugify import slugify
from ckeditor.fields import RichTextField
# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=50,null=True,blank=True)

    title = models.CharField(max_length=150,null=False,blank=False)
    description = models.CharField(max_length=300,null=False,blank=False)
    content = RichTextField()
    slug = models.SlugField(max_length=150,null=True,blank=True)
    is_delete = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Bloqlar"

    def save(self, *args, **kwargs):
        self.title = self.title.lower().replace("ş","s").replace("ç","c").replace("ü","u").replace("ı","i").replace("ğ","g").replace("ö","o").replace("ə","e")
        self.slug = slugify(self.title)
        super(Blog,self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title

    



