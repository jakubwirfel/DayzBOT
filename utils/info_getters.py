from datetime import datetime, timezone

import win32gui

from logger import Logger


class InfoGetters:
    @staticmethod
    def get_food_and_water_color() -> list:
        colorFood = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 1680, 990)
        colorWater = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 1630, 990)
        Logger.info(f"Food: {hex(colorFood)}")
        Logger.info(f"Water {hex(colorWater)}")
        return [hex(colorFood), hex(colorWater)]

    @staticmethod
    def get_current_time() -> str:
        current_time = datetime.now().strftime("%H:%M:%S")
        Logger.info(f"current time: {current_time}")
        return current_time

    @staticmethod
    def get_user_timezone() -> str:
        local_timezone = str(datetime.now(timezone.utc).astimezone().tzinfo)
        return local_timezone

    @staticmethod
    def return_restarts_time(time_zone: str, server_restarts: dict) -> list:
        for item, values in server_restarts.items():
            if time_zone == item:
                return values
