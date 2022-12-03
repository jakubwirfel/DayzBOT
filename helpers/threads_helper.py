from concurrent.futures import ThreadPoolExecutor

from player import Player


class ThreadHelper:
    def __init__(self):
        self.player = Player()

    def player_executor(self) -> None:
        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(self.player.sound_and_food_check)
            executor.submit(self.player.other_check)
