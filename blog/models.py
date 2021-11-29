from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=64)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return f"Post({self.title},{self.content})";

    def get_absolute_url(self):
        return reverse('blog-home')