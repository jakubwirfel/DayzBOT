from time import sleep

from helpers.key_mouse_helper import KeyMouseHelper
from logger import Logger
from utils.info_getters import InfoGetters


class RestartHelper:

    @staticmethod
    def counter_and_restart() -> None:
        current_time = InfoGetters.get_current_time()
        current_time = current_time[3:5:1]
        if 57 <= int(current_time) <= 59 or current_time == "00":
            Logger.info("fast exit")
            KeyMouseHelper.trigger_restart()
        else:
            time_to_restart = (57 - int(current_time)) * 60
            Logger.info(f"time to restart: {time_to_restart}")
            while time_to_restart:
                sleep(1)
                time_to_restart -= 1
            Logger.info("restart triggered")
            KeyMouseHelper.trigger_restart()
