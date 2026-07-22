from channels.generic.websocket import AsyncWebsocketConsumer
import json


class MainConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("connected")
        await self.accept()

    async def receive(self, text_data):
        data=json.loads(text_data)
        print(f"message recieved- {data}")

    async def disconnect(self, code):
        print(f"disconnected - close code- {code}")
        