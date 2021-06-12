import json
from django.contrib.auth.models import User
from .models import Message
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_id = "chat_%s" % self.room_id

        await self.channel_layer.group_add(
            self.room_group_id,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_id,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        handle = text_data_json['handle']
        user_id = text_data_json['user_id']
        profile_pic = text_data_json['profile_pic']

        await self.save_message(user_id=user_id, room_id=self.room_id, message=message)

        await self.channel_layer.group_send(
            self.room_group_id,
            {
                'type': 'chat_message',
                'message': message,
                'handle': handle,
                'user_id': user_id,
                'profile_pic': profile_pic
            }
        )

    async def chat_message(self, event):
        message = event['message']
        handle = event['handle']
        user_id = event['user_id']
        profile_pic = event['profile_pic']

        await self.send(text_data=json.dumps({
            'message': message,
            'handle': handle,
            'user_id': user_id,
            'profile_pic': profile_pic
        }))

    @sync_to_async
    def save_message(self, user_id, room_id, message):
        author = User.objects.get(pk=user_id)
        Message.objects.create(author=author, room_id=room_id, content=message)