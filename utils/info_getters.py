from datetime import datetime, timezone

from PIL import Image
from PIL import ImageGrab

from helpers.sound.sound_recorder_helper import SoundRecorderHelper
from logger import Logger
from utils.file_utils import FileUtils


class InfoGetters:
    @staticmethod
    def get_food_and_water_color() -> list:
        screenshot = ImageGrab.grab()
        path = fr"{FileUtils().checkers_path}\check_food.jpg"
        screenshot.save(path)
        im = Image.open(fr"{FileUtils().checkers_path}\check_food.jpg")
        pix = im.load()
        color_food = pix[1665, 995]
        color_water = pix[1625, 995]
        Logger.info(f"Food: {color_food}")
        Logger.info(f"Water {color_water}")
        return [color_food, color_water]

    @staticmethod
    def get_current_time() -> str:
        current_time = datetime.now(timezone.utc).strftime("%H:%M:%S")
        Logger.info(f"current time: {current_time}")
        return current_time

    @staticmethod
    def get_user_timezone() -> str:
        local_timezone = str(datetime.now(timezone.utc).astimezone().tzinfo)
        return local_timezone

    @staticmethod
    def return_recorded_sound() -> str:
        return SoundRecorderHelper().record()

    @staticmethod
    def get_menu_colors() -> list:
        screenshot = ImageGrab.grab()
        path = fr"{FileUtils().checkers_path}\check_menu.jpg"
        screenshot.save(path)
        im = Image.open(fr"{FileUtils().checkers_path}\check_menu.jpg")
        pix = im.load()
        color_logo1 = pix[150, 200]
        color_logo2 = pix[200, 200]
        color_logo3 = pix[350, 200]
        color_logo4 = pix[470, 200]
        Logger.info(f"Menu colors: {color_logo1, color_logo2, color_logo3, color_logo4}")
        return[color_logo1, color_logo2, color_logo3, color_logo4]

    @staticmethod
    def take_screenshot(path) -> str:
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        file: str = fr"{path}\screen{current_time}.jpg"
        screenshot = ImageGrab.grab()
        screenshot.save(file)
        return file

    @staticmethod
    def get_death_colors() -> list:
        screenshot = ImageGrab.grab()
        path = fr"{FileUtils().checkers_path}\check_death.jpg"
        screenshot.save(path)
        im = Image.open(fr"{FileUtils().checkers_path}\check_death.jpg")
        pix = im.load()
        color_1 = pix[150, 200]
        color_2 = pix[1600, 200]
        color_3 = pix[1600, 800]
        color_4 = pix[150, 800]
        Logger.info(f"Death colors: {color_1, color_2, color_3, color_4}")
        return [color_1, color_2, color_3, color_4]
