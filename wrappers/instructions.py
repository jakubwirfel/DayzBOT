from helpers.key_mouse_helper import KeyMouseHelper
from helpers.restart_helper import RestartHelper
from logger import Logger
from utils.decider import Decider
from utils.file_utils import FileUtils
from utils.info_getters import InfoGetters


class Instructions:
    def __init__(self, time_zone: str, server_restarts: dict):
        self.RESTART_TIME = InfoGetters.return_restarts_time(time_zone, server_restarts)

    @staticmethod
    def check_food() -> None:
        food_info = InfoGetters.get_food_and_water_color()
        Logger.info(F"is food ok: {Decider.verify_food_is_ok(food_info)}")
        if not Decider.verify_food_is_ok(food_info):
            KeyMouseHelper().eat_and_drink()

    def check_relog(self) -> None:
        current_time = InfoGetters.get_current_time()
        if Decider.check_time_to_restart(current_time, self.RESTART_TIME):
            RestartHelper.counter_and_restart()

    @staticmethod
    def check_sound() -> None:
        recorded_sound_path = InfoGetters.return_recorded_sound()
        FileUtils().remove_files_when_3()
        if Decider.verify_if_sound_occured(recorded_sound_path):
            Logger.info("Sound occured; send info to DC")