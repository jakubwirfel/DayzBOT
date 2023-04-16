import json
from typing import Any


class JsonHelper:
    @staticmethod
    def read_file(file_path: str) -> dict:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        return data

    @staticmethod
    def read_data(data: bytes) -> dict:
        return json.loads(data.decode("utf-8"))

    @staticmethod
    def save_file(file_path: str, content: Any) -> None:
        with open(file_path, "w") as json_file:
            json.dump(content, json_file)
