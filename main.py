from time import sleep
import os
from module_mercury import temp_cleaner

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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


main_menu()
options_menu()

while True:
    try:
        choice = input(f"{'Please select an option:':>58}")
        if choice == "1":
            temp_cleaner.download_delete()
            print('Deleting temporary files...')
            sleep(2)
            print(f'{'Temporary files deleted successfully!':>58}')
            sleep(2)
            clear_screen()
            main_menu()
            options_menu()
            
        elif choice == "2":
            print(f'{'Empty the recycle bin (2)':>58}')
        elif choice == "3":
            print(f'{'Memory optimization (3)':>56}')
        elif choice == "4":
            print(f'\033[1;31m{"Exit !":>39}\033[0m')
            sleep(1)
            print(f'\033[1;31m{"Good Bye !":>43}\033[0m')
            break
        else:
            print(f'{'\033[1;31mInvalid selection. Please try again.\033[0m':>72}')
            sleep(2)
            clear_screen()
            main_menu()
            options_menu()
            
    except ValueError:
        print(f'{'\033[1;31mInvalid input. Please enter a number.\033[0m'}')
        sleep(2)
        clear_screen()
        main_menu()
        options_menu()
        continue