from channels.generic.websocket import AsyncJsonWebsocketConsumer


class SensorsConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("sensors", self.channel_name)


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("sensors", self.channel_name)


    async def sensors(self, event):
        await self.send_json(event)
