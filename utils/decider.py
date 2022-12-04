from helpers.sound.sound_recognize_helper import SoundRecognizeHelper
from logger import Logger


class Decider:
    @staticmethod
    def verify_food_is_ok(food_colors: list) -> bool:
        for item in food_colors:
            r, g, b = item
            if (r >= 220 and g >= 230 and b <= 100) or (r >= 230 and g <= 100 and b <= 100):
                return True
        return False

    @classmethod
    def check_time_to_restart(cls, current_time: str, restarts_times: list) -> bool:
        closest_restart = cls.__find_closest_restart(current_time, restarts_times)
        print(closest_restart)
        if len(str(closest_restart)) == 1:
            closest_restart_minus_10: str = "0" + str(closest_restart - 1) + ":50"
            closest_restart_fixed = "0" + str(closest_restart) + ":00"
        else:
            closest_restart_minus_10: str = str(closest_restart - 1) + ":50"
            closest_restart_fixed = str(closest_restart) + ":00"
        current_time = current_time[0:5:1]
        print(current_time, closest_restart_minus_10, closest_restart_fixed)
        if closest_restart_minus_10 <= current_time <= closest_restart_fixed:
            Logger.info("restart now")
            return True
        Logger.info("no time for restart")
        return False

    @staticmethod
    def __find_closest_restart(current_time: str, restarts_times: list) -> int:
        try:
            output, index = min((i, idx) for idx, i in enumerate(restarts_times) if i > int(current_time[0:2:1]))
        except:
            output = restarts_times[0]
        return output

    @staticmethod
    def verify_if_sound_occured(sound_path: str) -> bool:
        sound_counter = SoundRecognizeHelper.recognize(sound_path)
        if sound_counter >= 5:
            return True
        return False

    @staticmethod
    def check_if_in_menu(menu_colors) -> bool:
        checkers = []
        if len(menu_colors) > 0:
            for item in menu_colors:
                r, g, b = item
                if r >= 200 and g >= 230 and b >= 220:
                    checkers.append(True)
                else:
                    checkers.append(False)
        return all(checkers)

    @staticmethod
    def check_if_dead(dead_colors) -> bool:
        checkers = []
        if len(dead_colors) > 0:
            for item in dead_colors:
                r, g, b = item
                if r <= 50 and g <= 50 and b <= 50:
                    checkers.append(True)
                else:
                    checkers.append(False)
        return all(checkers)
