from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True)
    comments = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.username