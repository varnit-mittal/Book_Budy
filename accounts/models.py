from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.

class newUser(AbstractUser):
    email=models.EmailField(max_length=60,unique=True)
    phone_number=models.CharField(max_length=11,unique=True)
    fav_books=models.CharField(max_length=300,null=True, blank=True)
    user_profile_image=models.ImageField(upload_to="profile",default='default.jpg')

    objects=UserManager()

    REQUIRED_FIELDS=['email','phone_number']