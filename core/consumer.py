import json
from channels.generic.websocket import AsyncWebsocketConsumer


class MainConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        print(text_data)


    async def disconnect(self, close_code):
        print(f"connection disconnected- {close_code}")