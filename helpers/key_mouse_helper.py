
from time import sleep

import pydirectinput


class KeyMouseHelper:
    _EAT_SLOT = 1
    _DRINK_SLOT = 2

    @staticmethod
    def eat_and_drink() -> None:
        sleep(1)
        pydirectinput.keyDown(f'{KeyMouseHelper._EAT_SLOT}')
        sleep(0.2)
        pydirectinput.keyUp(f'{KeyMouseHelper._EAT_SLOT}')
        sleep(2)
        pydirectinput.mouseDown(button='left')
        sleep(5)
        pydirectinput.mouseUp(button="left")
        KeyMouseHelper._EAT_SLOT = KeyMouseHelper._EAT_SLOT + 2
        sleep(1)
        pydirectinput.keyDown(f'{KeyMouseHelper._DRINK_SLOT}')
        sleep(0.2)
        pydirectinput.keyUp(f'{KeyMouseHelper._DRINK_SLOT}')
        sleep(2)
        pydirectinput.mouseDown(button='left')
        sleep(5)
        pydirectinput.mouseUp(button="left")
        KeyMouseHelper._DRINK_SLOT = KeyMouseHelper._DRINK_SLOT + 2
        print(f"Eat slot: {KeyMouseHelper._EAT_SLOT}, Drink slot: {KeyMouseHelper._DRINK_SLOT}")
        if KeyMouseHelper._EAT_SLOT == 10:
            _EAT_SLOT = 1
        if KeyMouseHelper._DRINK_SLOT == 9:
            _DRINK_SLOT = 2

    @classmethod
    def trigger_restart(cls) -> None:
        pydirectinput.keyDown('esc')
        sleep(0.2)
        pydirectinput.keyUp('esc')
        sleep(1)
        pydirectinput.moveTo(1600, 800)
        sleep(0.2)
        pydirectinput.mouseDown(button='left')
        sleep(0.5)
        pydirectinput.mouseUp(button="left")
        sleep(120)
        cls.turn_off_notifications()
        sleep(240)
        cls.trigger_join_to_server()

    @staticmethod
    def trigger_join_to_server() -> None:
        pydirectinput.moveTo(1600, 880)
        sleep(0.2)
        pydirectinput.mouseDown(button='left')
        sleep(0.5)
        pydirectinput.mouseUp(button="left")

    @staticmethod
    def turn_off_notifications() -> None:
        for i in range(640, 960, 40):
            pydirectinput.moveTo(950, i)
            pydirectinput.mouseDown(button='left')
            sleep(0.2)
            pydirectinput.mouseUp(button="left")
            sleep(0.5)
