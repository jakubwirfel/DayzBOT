from concurrent.futures import ThreadPoolExecutor

from player import Player


class ThreadHelper:
    def __init__(self):
        self.player = Player()

    def player_executor(self) -> None:
        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(self.player.food_and_water)
            executor.submit(self.player.restart)
