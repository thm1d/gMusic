from django.urls import path
from .views import RoomListView, RoomCreateView, GetRoom

urlpatterns = [
    path('room', RoomListView.as_view()),
    path('create-room', RoomCreateView.as_view()),
    path('get-room', GetRoom.as_view()),
]