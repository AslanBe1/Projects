from views import (
    create_user,
    add_contact,
    contact_list,
    create_chat,
    add_message,
    read_message,
    show_all_chats
)
from colorama import Fore


def menu():
    print(Fore.LIGHTWHITE_EX+'Create User  => 1'+Fore.RESET)
    print(Fore.LIGHTYELLOW_EX+"Add Contact  => 2"+Fore.RESET)
    print(Fore.MAGENTA+"Contact List => 3"+Fore.RESET)
    print(Fore.LIGHTGREEN_EX+"Create Chat  => 4"+Fore.RESET)
    print(Fore.GREEN+"Add Message  => 5"+Fore.RESET)
    print(Fore.LIGHTCYAN_EX+"Read Message => 6"+Fore.RESET)
    print(Fore.RED+'Exit         => q'+Fore.RESET)
    return input(Fore.YELLOW+"Enter Your Choice: "+Fore.RESET)


def run():
    while True:
        choice = menu()
        if choice == '1':
            user_id = input(Fore.CYAN+"User ID : "+Fore.RESET)
            password = input(Fore.CYAN+"password : "+Fore.RESET)
            phone_number = input(Fore.CYAN+"phone number : "+Fore.RESET)
            create_user(user_id, password, phone_number)
        elif choice == '2':
            user_id = input(Fore.MAGENTA+"User ID : "+Fore.RESET)
            contact_id = input(Fore.MAGENTA+"Contact ID : "+Fore.RESET)
            add_contact(user_id, contact_id)
        elif choice == '3':
            user_id = input(Fore.LIGHTMAGENTA_EX+"User ID : "+Fore.RESET)
            contact_list(user_id)
        elif choice == '4':
            user1 = input(Fore.BLUE+"User ID1 : "+Fore.RESET)
            user2 = input(Fore.BLUE+"User ID2 : "+Fore.RESET)
            create_chat(user1, user2)
        elif choice == '5':
            show_all_chats()
            chat_id = input(Fore.LIGHTYELLOW_EX+"Chat ID : "+Fore.RESET)
            add_message(chat_id)
        elif choice == '6':
            show_all_chats()
            chat_id = input(Fore.LIGHTYELLOW_EX+"Chat ID : "+Fore.RESET)
            read_message(chat_id)
        elif choice == 'q':
            print(Fore.LIGHTBLUE_EX+'Come back again'+Fore.RESET)
            break
        else:
            print(Fore.LIGHTRED_EX+'Choice Error'+Fore.RESET)


if __name__ == '__main__':
    run()


print('Hello world')
