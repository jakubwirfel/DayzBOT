import os
from typing import Final

from utils.json_helper import JsonHelper


class Config:
    CONFIG_PATH: Final[str] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..\\config.json")
    LOGS_PATH: Final[str] = JsonHelper.read_file(CONFIG_PATH)["LOGS_PATH"]
    SERVER_RESTARTS: Final[str] = JsonHelper.read_file(CONFIG_PATH)["SERVER_RESTARTS"]
    DISCORD_WEBHOOK: Final[str] = JsonHelper.read_file(CONFIG_PATH)["DISCORD_WEBHOOK"]
