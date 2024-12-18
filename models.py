import json
from enum import Enum
from typing import Optional
from datetime import datetime

class Language(Enum):
    RUSSIAN = 'ru'
    ENGLISH = 'en'
    UZBEK = 'uz'
    FRENCH = 'fr'


class User:
    def __init__(self,
                 user_id: str,
                 password: str,
                 phone_number: str,
                 full_name: Optional[str] = None,
                 language: Optional[Language] = None,
                 created_at: Optional[datetime] = None
                 ):
        self.user_id = user_id
        self.password = password
        self.phone_number = phone_number
        self.full_name = full_name
        self.language = language or Language.ENGLISH.value
        self.created_at = created_at or str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.contacts = []

    @staticmethod
    def load_users():
        with open("database/users.json", "r") as f:
            return json.load(f)

    @staticmethod
    def save_users(data):
        with open('database/users.json', 'w') as f:
            json.dump(data, f, indent=3)


class Message:
    def __init__(self, sender_id, receiver_id, body, timestamp: Optional[datetime] = None):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.body = body
        self.timestamp = timestamp or str(datetime.now())


class Chat:
    def __init__(self, chat_id, users):
        self.chat_id = chat_id
        self.users = users
        self.messages = []

    @staticmethod
    def load_chats():
        with open("database/chats.json", "r") as f:
            return json.load(f)

    @staticmethod
    def save_chats(data):
        with open('database/chats.json', 'w') as f:
            json.dump(data, f, indent=3)


class Channel:
    pass