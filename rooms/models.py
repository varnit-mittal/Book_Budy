from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=1000)
    participants=models.ManyToManyField(User,related_name='participants',blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-updated','-created']

    def __str__(self) -> str:
        return self.name

class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-updated','-created']

    def __str__(self) -> str:
        return self.body[0:50]