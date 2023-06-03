import psutil as psutil
from logger import Logger


class ProcessHelper:

    @staticmethod
    def is_process_running() -> bool:
        process_name = "DayZ_x64.exe"
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == process_name:
                return True
        Logger.warning("Please run DayZ_x64.exe")
        return False
