print("--- Attempting to load app.consumer ---")
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatRoomConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.chat_box_name = self.scope["url_route"]["kwargs"]["chat_box_name"]
        self.group_name = "chat_%s" % self.chat_box_name

        print(f"User connected to group: {self.group_name} with channel name: {self.channel_name}")

        await self.channel_layer.group_add(self.group_name,self.channel_name)
        await self.accept()
        print("WebSocket connection accepted.")

    async def disconnect(self, code):
        print(f"User disconnected from group: {self.group_name} with channel name: {self.channel_name}") 
        await self.channel_layer.group_discard(self.group_name,self.channel_name)

    async def receive(self, text_data=None):
        print(f"Received message from client: {text_data}") 
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        print(f"Sending message to group {self.group_name}: Message='{message}', Username='{username}'") 

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type" : "chatbox_message",
                "message" : message,
                "username" : username
            },
        )

    async def chatbox_message(self,event):
        print(f"Received group message event: {event} for channel: {self.channel_name}")
        message = event['message']
        username = event['username']

        print(f"Sending message back to client: Message='{message}', Username='{username}'")
        await self.send(
            text_data=json.dumps(
            {
                "message" : message,
                "username" : username
            }
            )
        )