import json
from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)

        await self.send(
            text_data=json.dumps({
                "message": data.get("message")
            })
        )

    async def disconnect(self, close_code):
        print(f"connection disconnected- {close_code}")