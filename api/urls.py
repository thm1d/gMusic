from django.urls import path
from .views import RoomListView, RoomCreateView, GetRoom, JoinRoomView, UserInRoom

urlpatterns = [
    path('room', RoomListView.as_view()),
    path('create-room', RoomCreateView.as_view()),
    path('get-room', GetRoom.as_view()),
    path('join-room', JoinRoomView.as_view()),
    path('user-in-room', UserInRoom.as_view()),
]