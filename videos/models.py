from django.db import models

# Create your models here.

class Channel(models.Model):
    name=models.CharField(max_length=200)
    token=models.CharField(max_length=600)
    uid=models.CharField(max_length=6)

class roomMember(models.Model):
    name=models.CharField(max_length=200)
    uid=models.CharField(max_length=200)
    room_name=models.CharField(max_length=200)

    def __str__(self):
        return self.name