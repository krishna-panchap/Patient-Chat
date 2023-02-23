from .config import Redis
from rejson import Path

class Cache:
    def __init__(self, json_client):
        self.json_client = json_client

    async def get_chat_history(self, token: str):
        data = self.json_client.jsonget(
            str(token), Path.rootPath())

        return data
    async def add_message_to_cache(self, token: str, message_data: dict):
        self.json_client.jsonarrappend(str(token), Path.rootPath(), message_data)

