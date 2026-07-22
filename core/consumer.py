from channels.generic.websocket import AsyncWebsocketConsumer
from core.models import MainDb


class MainConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user=self.scope["user"]
        if self.user.is_authenticated:
            self.group_name=f"user_{self.user}"
            await self.channel_layer.group_add(self.group_name, self.channel_name)
            print(f"{self.user.username} joined {self.group_name}")
            await self.accept()