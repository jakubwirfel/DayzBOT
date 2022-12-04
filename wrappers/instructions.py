from time import sleep

from helpers.discord_helper import DiscordHelper
from helpers.key_mouse_helper import KeyMouseHelper
from helpers.restart_helper import RestartHelper
from logger import Logger
from utils.decider import Decider
from utils.info_getters import InfoGetters


class Instructions:
    def __init__(self):
        self.SERVER_RESTARTS = [3, 7, 11, 15, 19, 23]
        self.__sound_counter = 0
        self.__sound_check_iteration = 0

    @staticmethod
    def check_food() -> None:
        food_info = InfoGetters.get_food_and_water_color()
        Logger.info(F"is food NOT ok: {Decider.verify_food_is_ok(food_info)}")
        if Decider.verify_food_is_ok(food_info):
            KeyMouseHelper().eat_and_drink()

    def check_relog(self) -> None:
        current_time = InfoGetters.get_current_time()
        if Decider.check_time_to_restart(current_time, self.SERVER_RESTARTS):
            RestartHelper.counter_and_restart()
            Instructions.check_if_in_menu()

    def check_sound(self) -> None:
        self.__sound_check_iteration += 1
        recorded_sound_path = InfoGetters.return_recorded_sound()
        if Decider.verify_if_sound_occured(recorded_sound_path):
            self.__sound_counter += 1
            if self.__sound_counter == 2:
                DiscordHelper().send_screen_massage(recorded_sound_path, "aaaaa kurwa RAJDUJĄ nas!")
        if self.__sound_check_iteration == 2:
            self.__sound_check_iteration = 0
            self.__sound_counter = 0

    @staticmethod
    def check_if_in_menu() -> None:
        menu_data = InfoGetters.get_menu_colors()
        Logger.info(F"is player in menu? {Decider.check_if_in_menu(menu_data)}")
        if Decider.check_if_in_menu(menu_data):
            KeyMouseHelper.turn_off_notifications()
            KeyMouseHelper.trigger_join_to_server()
            sleep(120)
            menu_data = InfoGetters.get_menu_colors()
            Logger.info(F"is player still in menu? {Decider.check_if_in_menu(menu_data)}")
            if Decider.check_if_in_menu(menu_data):
                screen_shot_path = InfoGetters.take_screenshot(r"C:\tmp\DayzBot\screenshot")
                DiscordHelper().send_screen_massage(screen_shot_path, "Nie wiem czemu, ale jestem w menu :(")

    @staticmethod
    def check_if_dead() -> None:
        death_data = InfoGetters.get_death_colors()
        Logger.info(F"is player dead? {Decider.check_if_dead(death_data)}")
        if Decider.check_if_dead(death_data):
            screen_shot_path = InfoGetters.take_screenshot(r"C:\tmp\DayzBot\screenshot")
            DiscordHelper().send_screen_massage(screen_shot_path, "Nie żyje :(")
