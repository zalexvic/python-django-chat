from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    handle = models.CharField(max_length=30, null=True)
    profile_pic = models.ImageField(default='images/default.jpg', upload_to='images/')


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=50, null=True)
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='my_rooms')
    users = models.ManyToManyField(User, related_name='all_rooms')


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    room_id = models.IntegerField(null=True)
    content = models.TextField(null=True)
    message_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-message_date']
