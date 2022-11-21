from logger import Logger


class Decider:
    @staticmethod
    def verify_food_is_ok(food_colors: list) -> bool:
        for item in food_colors:
            if 0xE9 <= int(item[6:8:1], 16) <= 0xFF:
                return False
        return True

    @classmethod
    def check_time_to_restart(cls, current_time: str, restarts_times: list) -> bool:
        closest_restart = cls.__find_closest_restart(current_time, restarts_times)
        current_time = current_time[0:5:1]
        closest_restart_minus_10: str = str(closest_restart - 1) + ":50"
        closest_restart_fixed = str(closest_restart) + ":00"
        if closest_restart_minus_10 <= current_time <= closest_restart_fixed:
            Logger.info("restart now")
            return True
        Logger.info("no time for restart")
        return False

    @staticmethod
    def __find_closest_restart(current_time: str, restarts_times: list) -> int:
        output, index = min((i, idx) for idx, i in enumerate(restarts_times) if i > int(current_time[0:2:1]))
        return output
