from django.urls import path
from core.consumer import MainConsumer

websocket_urlpatterns=[
    path("ws/abc/", MainConsumer.as_asgi())
]