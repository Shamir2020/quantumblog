from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=500,blank=False,null=False)
    creator = models.ForeignKey(User,on_delete=models.CASCADE,related_name='creator')
    content = RichTextField(blank=False,null=False)
    description = models.TextField(blank=False,null=False,default='')
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    name = models.CharField(max_length=300,blank=False,null=False)
    email = models.CharField(max_length=255,blank=False,null=False)
    image = models.ImageField(upload_to='profiles',null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE,related_name='usernameComment')
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blogComment')
    comment = models.TextField(blank=False,null=False)

    def __str__(self):
        return self.username


class Like(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE,related_name='usernameLike')
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blogLike')

    def __str__(self):
        return self.username
    



