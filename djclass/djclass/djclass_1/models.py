#argo
#1984
from django.db import models

from django.contrib.auth.models import AbstractUser



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/',null=True,blank=True)
    video = models.FileField(upload_to='videos/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class PythonModel(models.Model):
    title_p = models.CharField(max_length=200)
    content_p = models.TextField()
    photo_p = models.ImageField(upload_to='photos/',null=True,blank=True)
    video_p = models.FileField(upload_to='videos/',null=True,blank=True)
    created_at_p = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title_p
    
class webCCC(models.Model):
    title_c = models.CharField(max_length=200)
    content_c = models.TextField()
    photo_c = models.ImageField(upload_to='photos/',null=True,blank=True)
    video_c = models.ImageField(upload_to='videos/',null=True,blank=True)
    created_at_c = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_c
    
class webgo(models.Model):
    title_go = models.CharField(max_length=200)
    content_go = models.TextField()
    photo_go = models.ImageField(upload_to='photos/', null=True, blank=True)
    video_go = models.ImageField(upload_to='videos/', null=True, blank=True)
    created_at_go = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_go
    
class webjavascript(models.Model):
    title_js = models.CharField(max_length=200)
    content_js = models.TextField()
    photo_js =  models.ImageField(upload_to='photos/',null=True,blank=True)
    video_js = models.ImageField(upload_to='videos/',null=True,blank=True)



    def __str__(self):
        return self.title_js

