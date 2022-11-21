from utils.info_getters import InfoGetters


class Verifiers:
    def __init__(self):
        self.verify_user_timezone()

    @staticmethod
    def verify_user_timezone() -> None:
        time_zone = InfoGetters.get_user_timezone()
        if not time_zone == "Środkowoeuropejski czas stand." or time_zone == "GMT":
            raise Exception("Sorry, change your time zone tu UTC+1 or GMT")
