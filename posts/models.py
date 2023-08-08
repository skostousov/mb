from django.db import models

class Post(models.Model):
    text = models.TextField()#new databse model Post with field text, also specified content type
    def __str__(self):
        """A string representation of the model"""
        return self.text[:50]
# Create your models here.
