from django.urls import path
from .views import RoomListView, RoomCreateView

urlpatterns = [
    path('room_list', RoomListView.as_view()),
    path('room_create', RoomCreateView.as_view()),
]