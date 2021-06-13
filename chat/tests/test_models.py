from django.test import TestCase
from django.contrib.auth.models import User
from chat.models import Profile, Room, Message


class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user',
            password='test123'
        )

        self.room = Room.objects.create(
            creator=self.user,
            name='test room',
            password='testroom123',
        )
        self.room.users.add(self.user)

        self.profile = Profile.objects.create(
            user=self.user,
            handle='testhandle',
            profile_pic='images/default.png'
        )

        print("MODEL TEST SETUP", Room.objects.all())

    def test_user_creates_room(self):
        print("MODEL TEST ROOM", self.user.my_rooms.all())
        self.user.my_rooms.create(
            name='testroom2',
            password='testroom123',
        )
        print("MODEL TESTROOM2",Room.objects.all())
        self.assertEquals(Room.objects.get(name='testroom2').id, 3)

    def test_user_creates_message(self):
        print("MODEL TEST MSG", Room.objects.all())
        self.user.message_set.create(
            room_id=1,
            content='test_message'
        )

        self.assertEquals(Message.objects.get(id=1).room_id, 1)
        self.assertEquals(Message.objects.get(author=self.user).content, 'test_message')

        print("MODEL TEST MSG2", Room.objects.all())