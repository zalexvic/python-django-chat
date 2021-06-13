from django.test import SimpleTestCase
from django.urls import reverse, resolve
from register.views import sign_up
from chat.views import (
    index,
    room,
    create_room,
    edit_room,
    enter_room,
    join_room,
    all_rooms,
    profile,
    load_more
)


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_room_url_is_resolved(self):
        url = reverse('room', args=['1'])
        self.assertEquals(resolve(url).func, room)

    def test_create_room_url_is_resolved(self):
        url = reverse('create_room')
        self.assertEquals(resolve(url).func, create_room)

    def test_edit_room_url_is_resolved(self):
        url = reverse('edit_room', args=['1'])
        self.assertEquals(resolve(url).func, edit_room)

    def test_enter_room_url_is_resolved(self):
        url = reverse('enter_room', args=['1'])
        self.assertEquals(resolve(url).func, enter_room)

    def test_join_room_url_is_resolved(self):
        url = reverse('join_room')
        self.assertEquals(resolve(url).func, join_room)

    def test_all_rooms_url_is_resolved(self):
        url = reverse('all_rooms')
        self.assertEquals(resolve(url).func, all_rooms)

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_load_more_url_is_resolved(self):
        url = reverse('load_more', args=['1'])
        self.assertEquals(resolve(url).func, load_more)

    def test_sign_up_url_is_resolved(self):
        url = reverse('sign_up')
        self.assertEquals(resolve(url).func, sign_up)