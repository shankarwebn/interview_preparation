from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class PostConsumer(WebsocketConsumer):

    def connect(self):
        print("CONNECTED")

        self.group_name = "posts"
        print("CONNECTED")

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):

        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def send_post(self, event):

        self.send(text_data=json.dumps({
            'title': event['title']
        }))