from django.test import TestCase
from register.forms import RegisterForm
from chat.forms import (
    CreateRoomForm,
    EditProfileForm,
    EnterRoomForm,
    JoinRoomForm,
    EditRoomForm
)


class TestForms(TestCase):

    def test_create_room_form(self):
        form = CreateRoomForm(data={
            'room_name': 'rooooom123',
            'room_password': 'password123'
        })
        self.assertTrue(form.is_valid())

        form = CreateRoomForm(data={
            'room_name': 'rooooom123'
        })
        self.assertFalse(form.is_valid())

        form = CreateRoomForm(data={
            'room_name': 'name',
            'room_password': '5'*51
        })
        self.assertFalse(form.is_valid())

    def test_edit_profile_form(self):
        form = EditProfileForm(data={
            'handle': '123nickname123'
        })
        self.assertTrue(form.is_valid())

        form = EditProfileForm(data={
            'handle': 'xxx'*20
        })
        self.assertFalse(form.is_valid())

    def test_enter_room_form(self):
        form = EnterRoomForm(data={
            'password': 'password123'
        })
        self.assertTrue(form.is_valid())

        form = EnterRoomForm(data={
            'password': 'pass'*20
        })
        self.assertFalse(form.is_valid())

    def test_join_room_form(self):
        form = JoinRoomForm(data={
            'room_id': 37
        })
        self.assertTrue(form.is_valid())

        form = JoinRoomForm(data={})
        self.assertFalse(form.is_valid())

    def test_edit_room_form(self):
        form = EditRoomForm(data={
            'room_name': 'roomname123',
            'password': 'password123'
        })
        self.assertTrue(form.is_valid())

        form = EditRoomForm(data={})
        self.assertTrue(form.is_valid())

        form = EditRoomForm(data={
            'room_name': 'roomname123'
        })
        self.assertTrue(form.is_valid())

        form = EditRoomForm(data={
            'room_password': 'password123'
        })
        self.assertTrue(form.is_valid())

        form = EditRoomForm(data={
            'room_name': 'roomname123'*100,
            'room_password': 'password123'
        })
        self.assertFalse(form.is_valid())

        form = EditRoomForm(data={
            'room_name': 'roomname123',
            'room_password': 'password123'*10
        })
        self.assertFalse(form.is_valid())

    def test_register_form(self):
        form = RegisterForm(data={
            'username': 'user_name_123',
            'handle': 'handle123',
            'password1': 'password123password',
            'password2': 'password123password'
        })
        self.assertTrue(form.is_valid())

        form = RegisterForm(data={
            'username': 'user_name_123',
            'handle': 'handle123',
            'password1': 'password123password',
            'password2': 'password124password'
        })
        self.assertFalse(form.is_valid())

        form = RegisterForm(data={
            'username': 'user_name_123',
            'password1': 'password123password',
            'password2': 'password123password'
        })
        self.assertFalse(form.is_valid())

        form = RegisterForm(data={
            'username': 'user_name_123',
            'handle': 'handle123',
            'password1': 'password123password'
        })
        self.assertFalse(form.is_valid())