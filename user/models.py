from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=30)
    password = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    comments = models.TextField(max_length=200)

    def __str__(self):
        return self.username