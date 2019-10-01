from django.db import models

# Create your models here.

from user_profile.models import User

class Post(models.Model):
    user = models.ForeignKey('user_profile.User',on_delete=models.CASCADE)
    text = models.CharField(max_length = 240)
    created_date = models.DateTimeField(auto_now_add= True)
    location = models.CharField(max_length= 30, default='Russia')
    is_active = models.BooleanField(default= True)
    is_favorite = models.BooleanField(default= False)

    def __str__(self):
        return self.text[:50]