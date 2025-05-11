print("--- Attempting to load chat.routing ---")

from django.urls import re_path
from app import consumer

websocket_urlpatterns = [
    re_path(
        r"ws/chat/(?P<chat_box_name>\w+)/$", consumer.ChatRoomConsumer.as_asgi()

    )
]