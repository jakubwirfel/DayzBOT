from helpers.threads_helper import ThreadHelper
from player import Player
from utils.file_utils import FileUtils

# ToDo link to discord w json


menu_options = {
    1: 'Anti Ride',
    2: 'Ride Mele',
}


def print_menu():
    print("\n===========PREPARE===========\n"
          "- Make sure that config.json in in main DayzBOT folder\n"
          "- Please verify server restart in config.json\n"
          "- Set LOGS_PATH in config.json\n"
          "==================================")
    print("\n===========REQUIREMENTS===========\n"
          "- user resolution: 1920 x 1080\n"
          "- sound card with loopback\n"
          "- OS: Windows 10 / 11\n"
          "- No game filters\n"
          "- No earplugs\n"
          "- Max total volume in game\n"
          "- Max effects volume in game\n"
          "- 50% windows volume\n"
          "==================================\n")
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def anti_ride():
    FileUtils()
    ThreadHelper().player_executor()


def ride_mele():
    Player().player_ride_mele()


def option3():
    print('Handle option \'Option 3\'')


if __name__ == "__main__":
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except KeyboardInterrupt:
            exit()
        if option == 1:
            anti_ride()
        elif option == 2:
            ride_mele()
        else:
            print('Invalid option. Please enter a number 1.')
