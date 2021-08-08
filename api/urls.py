from django.urls import path
from .views import RoomListView, RoomCreateView

urlpatterns = [
    path('room', RoomListView.as_view()),
    path('create-room', RoomCreateView.as_view())
]