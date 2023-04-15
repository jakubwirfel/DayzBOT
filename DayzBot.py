from helpers.threads_helper import ThreadHelper
from utils.file_utils import FileUtils

menu_options = {
    1: 'Anti Ride',
    2: 'Riding 10min',
    3: 'Option 3',
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def option1():
    FileUtils()
    ThreadHelper().player_executor()


def option2():
    print('Handle option \'Option 2\'')


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
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        else:
            print('Invalid option. Please enter a number between 1 and 3.')
