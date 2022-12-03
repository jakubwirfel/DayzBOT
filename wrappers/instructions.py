from time import sleep

from helpers.discord_helper import DiscordHelper
from helpers.key_mouse_helper import KeyMouseHelper
from helpers.restart_helper import RestartHelper
from logger import Logger
from utils.decider import Decider
from utils.info_getters import InfoGetters


class Instructions:
    def __init__(self, server_restarts: list):
        self.RESTART_TIME = server_restarts

    @staticmethod
    def check_food() -> None:
        food_info = InfoGetters.get_food_and_water_color()
        Logger.info(F"is food NOT ok: {Decider.verify_food_is_ok(food_info)}")
        if Decider.verify_food_is_ok(food_info):
            KeyMouseHelper().eat_and_drink()

    def check_relog(self) -> None:
        current_time = InfoGetters.get_current_time()
        if Decider.check_time_to_restart(current_time, self.RESTART_TIME):
            RestartHelper.counter_and_restart()

    @staticmethod
    def check_sound() -> None:
        recorded_sound_path = InfoGetters.return_recorded_sound()
        if Decider.verify_if_sound_occured(recorded_sound_path):
            DiscordHelper().send_screen_massage(recorded_sound_path, "aaaaa kurwa RAJDUJĄ nas!")

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
