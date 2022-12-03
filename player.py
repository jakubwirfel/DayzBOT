from time import sleep

from logger import Logger
from utils.file_utils import FileUtils
from wrappers.instructions import Instructions


class Player:
    SERVER_RESTARTS = [3, 7, 11, 15, 19, 23]

    def __init__(self):
        self.instructions = Instructions(Player.SERVER_RESTARTS)

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
            Logger.info("-------------------FOOD CHECK FINISH WAITING 600S")
            Logger.info("-------------------Sound CHECK")
            self.instructions.check_sound()
            Logger.info("-------------------Sound and food CHECK FINISH WAITING 60S")
            FileUtils().remove_audio_files_when_3()
            FileUtils().delete_files()
            sleep(60)
