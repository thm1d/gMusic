from django.urls import path
from .views import RoomListView, RoomCreateView

urlpatterns = [
    path('room-list', RoomListView.as_view()),
    path('room-create', RoomCreateView.as_view()),
]