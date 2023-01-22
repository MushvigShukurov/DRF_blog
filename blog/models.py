from django.db import models
from slugify import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Blog(models.Model):
    # author = models.CharField(max_length=50,null=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="bloqlar")

    title = models.CharField(max_length=150,null=False,blank=False)
    description = models.CharField(max_length=300,null=False,blank=False)
    content = RichTextField()
    slug = models.SlugField(max_length=150,null=True,blank=True)
    is_delete = models.BooleanField(default=False)
    
    # raiting = models.IntegerField(validators=[MinValueValidator,MaxValueValidator],default=0)
    # many to many olmalidir reytinq bir user bir cox kitaba ulduz vere biler
    # bir kitaba birden cox user ulduz vere biler

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

    
class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="comments")
    # comment_author_firstname = models.CharField(max_length=50)
    # comment_author_lastname = models.CharField(max_length=50)
    # comment_author_email = models.CharField(max_length=100)

    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_comments")

    comment_text = models.TextField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class BlogRaiting(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="raitings")
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE, related_name="raitings")
    raiting = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=5)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




    def save(self, *args, **kvargs):
        raitings_for_user = BlogRaiting.objects.filter(user=self.user,blog=self.blog).count()
        if raitings_for_user == 0:
            super(BlogRaiting,self).save(*args,**kvargs)
        elif raitings_for_user == 1:
            up_raiting = BlogRaiting.objects.filter(user=self.user,blog=self.blog).first()
            self.created_at = up_raiting.created_at
            up_raiting.delete()
            super(BlogRaiting,self).save(*args,**kvargs)





    def __str__(self) -> str:
        return "BLOG: " + self.blog.title + " | Reytinq: " + str(self.raiting) + " | " + "USER :" + self.user.username
