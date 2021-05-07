from django.db import models
from django.urls import reverse
#from taggit.managers import TaggableManager

# Create your models here.
class Blog(models.Model):
    discription = models.TextField()
    timecase = models.DateTimeField( auto_now_add=True)
    thumbnail = models.ImageField(upload_to='album/skalaminhossain/')


class Personalblog(models.Model):
    blogtitle = models.TextField()
    slug = models.SlugField()
    description = models.TextField()
    timecase = models.DateTimeField( auto_now_add=True)
    #tags =TaggableManager()
    thumbnail = models.ImageField(upload_to='album/skalaminhossain/')
    
    def __str__(self):
        return self.blogtitle

    def get_absolute_url(self):
        return reverse("blog:blogDetails", kwargs={"slug": self.slug})

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()
    

class Comment(models.Model):
    post = models.ForeignKey(Personalblog, on_delete= models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
