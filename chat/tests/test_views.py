from django.test import TestCase
from django.urls import reverse
from chat.models import Profile, Room, Message
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        self.index_url = reverse('index')
        self.room_url = reverse('room', args=['1'])
        self.create_room_url = reverse('create_room')
        self.edit_room_url = reverse('edit_room', args=['1'])
        self.enter_room_url = reverse('enter_room', args=['1'])
        self.join_room_url = reverse('join_room')
        self.all_rooms_url = reverse('all_rooms')
        self.profile_url = reverse('profile')
        self.load_more_url = reverse('load_more', args=['1'])
        self.sign_up_url = reverse('sign_up')

        self.user = User.objects.create_user(
            username='test_user',
            password='testuser123'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            handle='test_handle',
            profile_pic='images/default.png'
        )

        self.client.force_login(self.user)

    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/index.html')

    def test_room_GET(self):
        room1 = Room.objects.create(
            id=1,
            creator=self.user,
            name='test_room1',
            password='test123'
        )
        room1.users.add(self.user)

        response = self.client.get(self.room_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/room.html')

    def test_create_room_POST(self):
        response = self.client.post(self.create_room_url, {
            'room_name': 'Test Room 2',
            'room_password': 'test321'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Room.objects.get(name='Test Room 2').name, 'Test Room 2')

    def test_edit_room_POST(self):
        room1 = Room.objects.create(
            id=1,
            creator=self.user,
            name='test_room1',
            password='test123'
        )
        room1.users.add(self.user)

        response = self.client.post(self.edit_room_url, {
            'room_name': 'edited name'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Room.objects.get(id=1).name, 'edited name')

    def test_enter_room_POST(self):
        Room.objects.create(
            id=1,
            creator=self.user,
            name='test_room1',
            password='test123'
        )

        response = self.client.post(self.enter_room_url, {
            'password': 'test123'
        })
        self.assertEquals(response.status_code, 302)

        response = self.client.get(self.room_url)
        self.assertEquals(response.status_code, 200)

    def test_join_room_user_in_room_POST(self):
        room1 = Room.objects.create(
            id=1,
            creator=self.user,
            name='test_room1',
            password='test123'
        )
        room1.users.add(self.user)

        response = self.client.post(self.join_room_url, {
            'room_id': '1'
        })
        self.assertEquals(response.status_code, 302)

        response = self.client.get(self.room_url)
        self.assertEquals(response.status_code, 200)

    def test_join_room_use_not_in_room_POST(self):
        Room.objects.create(
            id=1,
            creator=self.user,
            name='test_room1',
            password='test123'
        )

        response = self.client.post(self.join_room_url, {
            'room_id': '1'
        })
        self.assertEquals(response.status_code, 302)

        response = self.client.get(self.enter_room_url)
        self.assertEquals(response.status_code, 200)

    def test_all_rooms_GET(self):
        response = self.client.get(self.all_rooms_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/all-rooms.html')

    def test_profile_POST(self):
        response = self.client.post(self.profile_url, {
            'handle': 'edited handle'
        })

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Profile.objects.get(handle='edited handle').handle, 'edited handle')

    def test_sign_up_POST(self):
        response = self.client.post(self.sign_up_url, {
            'username': 'testuser2',
            'handle': 'testhandle 2',
            'password1': 'password123password',
            'password2': 'password123password'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.get(username='testuser2').username, 'testuser2')