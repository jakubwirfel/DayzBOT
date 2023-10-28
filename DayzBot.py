from helpers.process_helper import ProcessHelper
from helpers.threads_helper import ThreadHelper
from logger import Logger
from player import Player
from utils.file_utils import FileUtils

# ToDo
#  link to discord w json
#  dodanie autoruna
#  dodanie earplugs

menu_options = {
    1: "Anti Ride",
    2: "Ride Mele",
    "e": "Exit"
}


def print_menu() -> None:
    print(f"\nCtrl+C -- exit script or choice interruption\n")
    for key in menu_options.keys():
        print(key, "--", menu_options[key])


def print_requirements() -> None:
    print("\n===================PREPARE===================\n"
          "- Make sure that config.json in in main DayzBOT folder\n"
          "- Please verify server restart in config.json\n"
          "- Set LOGS_PATH in config.json")
    print("===========REQUIREMENTS ANTI RIDE===========\n"
          "- user resolution: 1920 x 1080\n"
          "- sound card with loopback\n"
          "- OS: Windows 10 / 11\n"
          "- No game filters\n"
          "- No earplugs\n"
          "- Max total volume in game\n"
          "- Max effects volume in game\n"
          "- 50% windows volume\n"
          "============================================")


def anti_ride():
    FileUtils()
    ThreadHelper.player_executor()


def ride_mele():
    Player().player_ride_mele()


def option3():
    print('Handle option \'Option 3\'')


if __name__ == "__main__":
    if ProcessHelper.is_process_running():
        requirements_print = True
        while True:
            if requirements_print:
                print_requirements()
                requirements_print = False
            print_menu()
            option = ''
            try:
                option = str(input("Enter your choice: "))
            except KeyboardInterrupt:
                Logger.info("\nKeyboard Interrupt exiting...")
                exit()
            if option == "1":
                anti_ride()
            elif option == "2":
                ride_mele()
            elif any(["e", "E"]):
                Logger.info("\nExiting...")
                exit()
            else:
                Logger.warning(f"Invalid option ({option}). Please enter a number 1 or 2")
