from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_avatar = models.ImageField(null=True, blank=True)


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=200)
    room_password = models.CharField(max_length=50)
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_creator')
    users = models.ManyToManyField(User, related_name='users')


class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    user_author = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message_date = models.DateTimeField(auto_now_add=True)
