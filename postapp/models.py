from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="img")
    tags = models.ManyToManyField("Tag", related_name="tags")
    
    def __str__(self):
        return self.title 


class Tag(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    