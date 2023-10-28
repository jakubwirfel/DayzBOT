
import time
from concurrent.futures import ThreadPoolExecutor

from logger import Logger
from player import Player


class ThreadHelper:
    event = True

    @staticmethod
    def player_executor() -> None:
        player = Player()
        executor = ThreadPoolExecutor(max_workers=2)
        future1 = executor.submit(player.sound_and_food_check)
        future2 = executor.submit(player.other_check)

        try:
            while not (future1.done() and future2.done()):
                time.sleep(1)
        except KeyboardInterrupt:
            ThreadHelper.event = False
            executor.shutdown(wait=False)
            Logger.info("ANTI RIDE FINISHED BY USER")
