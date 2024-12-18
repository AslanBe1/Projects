import utils
from app.models import Chat, Message
from models import User
from colorama import Fore

def create_user(user_id: str, password: str, phone_number: str):
    users_data: dict = User.load_users()
    if user_id in users_data:
        print(Fore.LIGHTRED_EX+"User already exists"+Fore.RESET)
    else:
        user = User(user_id=user_id, password=password, phone_number=phone_number)
        user.password = str(utils.hash_password(password))
        users_data[user_id] = user.__dict__
        User.save_users(users_data)
        print(Fore.LIGHTGREEN_EX+"User successfully created!"+Fore.RESET)


def add_contact(user_id, contact_id):
    users_data: dict = User.load_users()
    if (user_id and contact_id) not in users_data:
        print(Fore.LIGHTRED_EX+"User does not exists"+Fore.RESET)
    elif user_id == contact_id:
        print(Fore.LIGHTRED_EX+"IDs must not be equal"+Fore.RESET)
    elif contact_id in users_data[user_id]["contacts"]:
        print(Fore.LIGHTRED_EX+"This contact id already exists"+Fore.RESET)
    else:
        users_data[user_id]["contacts"].append(contact_id)

        User.save_users(users_data)

        print(Fore.LIGHTGREEN_EX+"Contact successfully added!"+Fore.RESET)


def contact_list(user_id):
    users_data = User.load_users()
    if user_id not in users_data:
        print(Fore.LIGHTRED_EX+"User does not exists"+Fore.RESET)
    else:
        print(Fore.LIGHTYELLOW_EX+f"{user_id}'s contacts : {users_data[user_id]['contacts']}"+Fore.RESET)


def create_chat(user1, user2):
    chat_id = f"{user1} -> {user2}"
    chats_data = Chat.load_chats()
    if (user1 and user2) not in User.load_users():
        print(Fore.LIGHTRED_EX+"You cannot create chat.Because there is not enough user"+Fore.RESET)
        return

    if chat_id in chats_data:
        print(Fore.LIGHTRED_EX+"Chat is already exists"+Fore.RESET)
        return

    chat = Chat(chat_id, users=[user1, user2])
    chats_data[chat_id] = chat.__dict__
    Chat.save_chats(chats_data)
    print(Fore.LIGHTGREEN_EX+"Chat successfully created"+Fore.RESET)



def add_message(chat_id):
    chats_data = Chat.load_chats()
    if chat_id not in Chat.load_chats():
        print(Fore.LIGHTRED_EX+"Chat does not exist"+Fore.RESET)
        return

    sender = input("Sender ID : ")
    receiver = input("Receiver ID : ")
    chat = chats_data[chat_id]
    if sender not in chat['users']:
        print(Fore.LIGHTRED_EX+"Sender does not exist"+Fore.RESET)

    if receiver not in chat['users']:
        print(Fore.LIGHTRED_EX+"Receiver does not exist"+Fore.RESET)
    else:
        body = input(f"body : ")
        message = Message(sender,   receiver, body)
        chats_data[chat_id]["messages"].append(message.__dict__)
        Chat.save_chats(chats_data)
        print(Fore.LIGHTGREEN_EX+"Message successfully sent"+Fore.RESET)


def read_message(chat_id):
    chats_data = Chat.load_chats()
    if chat_id not in chats_data:
        print(Fore.LIGHTRED_EX+"Chat does not exist"+Fore.RESET)
        return

    chat = chats_data[chat_id]
    if not chat["messages"]:
        print(Fore.LIGHTRED_EX+"No messages in this chat"+Fore.RESET)
        return
    print(Fore.LIGHTYELLOW_EX+f"Messages in chat {chat_id}:\n"+Fore.RESET)

    for message in chat["messages"]:
        if message["sender_id"] == chat["users"][0]:
            print(f'{' '*30}{message['timestamp']}')
            print(Fore.LIGHTWHITE_EX+f"{message['sender_id']}: {message['body']}\n"+Fore.RESET)
        else:
            print(f'{' '*30}{message['timestamp']}')
            print(Fore.LIGHTWHITE_EX+f"{'        ' * 8}{message['sender_id']}: {message['body']}"+Fore.RESET)


def show_all_chats():
    chats_data = Chat.load_chats()
    for chat in chats_data:
        print(chat)