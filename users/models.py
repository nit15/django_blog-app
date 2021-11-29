from django.db import models
from django.contrib.auth.models import User
from PIL import  Image

# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    image=models.ImageField(default='default.jpg',upload_to='profile_pic')


    def __str__(self):
        return f"{self.user.username} Profile"


    def save(self):
        super().save()
        img=Image.open(self.image.path)

        if img.width>300 or img.height>300:
            outputsize=(300,300)
            img.thumbnail(outputsize)
            img.save(self.image.path)