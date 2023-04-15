from time import sleep
from helpers.key_mouse_helper import KeyMouseHelper
from logger import Logger
from utils.file_utils import FileUtils
from wrappers.instructions import Instructions


class Player:

    def __init__(self):
        self.instructions = Instructions()

    def other_check(self) -> None:
        sleep(5)
        while True:
            Logger.info("-------------------Menu CHECK")
            self.instructions.check_if_in_menu()
            Logger.info("-------------------Menu CHECK FINISH WAITING 600S")
            Logger.info("-------------------Death CHECK")
            self.instructions.check_if_dead()
            Logger.info("-------------------Death CHECK FINISH WAITING 600S")
            Logger.info("-------------------RESTART CHECK")
            self.instructions.check_relog()
            Logger.info("-------------------RESTART CHECK FINISH WAITING 600S")
            FileUtils().delete_files()
            sleep(600)

    def sound_and_food_check(self) -> None:
        sleep(60)
        while True:
            Logger.info("-------------------FOOD CHECK")
            self.instructions.check_food()
            Logger.info("-------------------FOOD CHECK FINISH WAITING 60S")
            Logger.info("-------------------Sound CHECK")
            self.instructions.check_sound()
            Logger.info("-------------------Sound and food CHECK FINISH WAITING 60S")
            FileUtils().remove_audio_files_when_3()
            FileUtils().delete_files()
            sleep(60)

    def player_ride_mele(self) -> None:
        sleep(5)
        Logger.info("---------STARTING MELE RIDE")
        try:
            KeyMouseHelper.ride_mele()
        except KeyboardInterrupt:
            Logger.info("---------MELE RIDE FINISHED BY USER")
            KeyMouseHelper.finished_mele_ride()
