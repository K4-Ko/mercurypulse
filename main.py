from time import sleep
import os

def print_centered(text):
    terminal_width = os.get_terminal_size().columns
    print(text.center(terminal_width))

def main_menu():
    menu_art = [
        "▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄",
        "▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄",
        "███████████████████████████████████████████████████████████████████████████████",
        "█▄─▀█▀─▄█▄─▄▄─█▄─▄▄▀█─▄▄▄─█▄─██─▄█▄─▄▄▀█▄─█─▄███▄─▄▄─█▄─██─▄█▄─▄███─▄▄▄▄█▄─▄▄─█",
        "██─█▄█─███─▄█▀██─▄─▄█─███▀██─██─███─▄─▄██▄─▄█████─▄▄▄██─██─███─██▀█▄▄▄▄─██─▄█▀█",
        "▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▀▄▄▀▀▄▄▄▀▀▀▀▄▄▄▀▀▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀",
        "",
        "        █▀ █▄█ █▀ ▀█▀ █▀▀ █▀▄▀█   █▀█ █▀█ ▀█▀ █ █▀▄▀█ █ ▀█ █▀▀ █▀█",
        "        ▄█ ░█░ ▄█ ░█░ ██▄ █░▀░█   █▄█ █▀▀ ░█░ █ █░▀░█ █ █▄ ██▄ █▀▄",
        "",
        "▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄"
    ]
    for line in menu_art:
        print_centered(line)

def options_menu():
    menu_text = [
        "Clean temporary files (1)",
        "Empty the recycle bin (2)",
        "Memory optimization (3)",
        "Exit (4)"
    ]
    print("\033[1m")  
    for line in menu_text:
        print_centered(line)
    print("\033[0m")  

main_menu()
options_menu()

while True:
    try:
        choice = input(f'{'Please select an option: ':>50}')
        if choice == "1":
            print(f'{'Clean temporary files (1)':>50}')
        elif choice == "2":
            print(f'{'Empty the recycle bin (2)':>50}')
        elif choice == "3":
            print(f'{'Memory optimization (3)':>48}')
        elif choice == "4":
            print(f'\033[1;31m{"Exit !":>31}\033[0m')
            sleep(1)
            print(f'\033[1;31m{"Good Bye !":>35}\033[0m')
            break
        else:
            print(f'{'\033[1;31mInvalid selection. Please try again.\033[0m':>72}')
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            main_menu()
            options_menu()
            
    except ValueError:
        print(f'{'\033[1;31mInvalid input. Please enter a number.\033[0m'}')
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        main_menu()
        options_menu()
        continue