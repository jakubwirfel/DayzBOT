from time import sleep

from logger import Logger
from utils.info_getters import InfoGetters
from wrappers.instructions import Instructions


class Player:
    SERVER_RESTARTS = {
        "Środkowoeuropejski czas stand.": [4, 8, 12, 16, 20, 24],
        "GMT": [3, 7, 11, 15, 19, 23]
    }

    CURRENT_TIMEZONE = InfoGetters.get_user_timezone()

    def __init__(self):
        self.instructions = Instructions(Player.CURRENT_TIMEZONE, Player.SERVER_RESTARTS)

    def food_and_water(self) -> None:
        sleep(10)
        while True:
            Logger.info("-------------------FOOD CHECK")
            self.instructions.check_food()
            Logger.info("-------------------FOOD CHECK FINISH WAITING 600S")
            sleep(600)

    def restart(self) -> None:
        sleep(13)
        while True:
            Logger.info("-------------------RESTART CHECK")
            self.instructions.check_relog()
            Logger.info("-------------------RESTART CHECK FINISH WAITING 600S")
            sleep(600)

    def restart(self) -> None:
        sleep(13)
        while True:
            Logger.info("-------------------RESTART CHECK")
            self.instructions.check_relog()
            Logger.info("-------------------RESTART CHECK FINISH WAITING 600S")
            sleep(600)