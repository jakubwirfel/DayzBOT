
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
        if KeyMouseHelper._EAT_SLOT == 10:
            _EAT_SLOT = 1
        if KeyMouseHelper._DRINK_SLOT == 9:
            _DRINK_SLOT = 2

    @staticmethod
    def trigger_restart() -> None:
        pydirectinput.keyDown('esc')
        sleep(0.2)
        pydirectinput.keyUp('esc')
        sleep(1)
        pydirectinput.moveTo(1600, 800)
        sleep(0.2)
        pydirectinput.mouseDown(button='left')
        sleep(0.5)
        pydirectinput.mouseUp(button="left")
        sleep(360)
        pydirectinput.moveTo(1600, 880)
        sleep(0.2)
        pydirectinput.mouseDown(button='left')
        sleep(0.5)
        pydirectinput.mouseUp(button="left")
