import json
from channels.generic.websocket import AsyncWebsocketConsumer
from core.models import MainDb


class MainConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        print(text_data)
        await MainDb.objects.acreate(message=text_data)
        await self.send(text_data="data saved in the database")
       
    async def disconnect(self, close_code):
        print(f"connection disconnected- {close_code}")