from django.urls import path

from . import views

urlpatterns = [
    path('join-room/', views.join_room, name='join_room'),
    path('edit-room/<int:room_id>', views.edit_room, name='edit_room'),
    path('enter-room/<int:room_id>', views.enter_room, name='enter_room'),
    path('<int:room_id>/', views.room, name='room')
]