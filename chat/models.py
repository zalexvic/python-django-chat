from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='users')


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message_date = models.DateTimeField(auto_now_add=True)
