import os

from logger import Logger
import os, shutil

class FileUtils:
    def __init__(self):
        self.main_path = r'C:\tmp\DayzBot'
        self.photo_path = r'C:\tmp\DayzBot\screenshot'
        self.audio_path = r'C:\tmp\DayzBot\audio'
        self.checkers_path = r'C:\tmp\DayzBot\checkers'

        self.create_data_folder(self.main_path)
        self.create_data_folder(self.audio_path)
        self.create_data_folder(self.photo_path)
        self.create_data_folder(self.checkers_path)

    @staticmethod
    def create_data_folder(folder_name) -> None:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

    def remove_audio_files_when_3(self) -> None:
        list_of_files = os.listdir(self.audio_path)
        full_path = [fr"{self.audio_path}\\{x}" for x in list_of_files]
        if len(list_of_files) >= 3:
            Logger.info("Start removing audio files")
            oldest_file = min(full_path, key=os.path.getctime)
            os.remove(oldest_file)
            Logger.info(f"File deleted: {oldest_file}")

    def delete_files(self) -> None:
        for filename in os.listdir(self.checkers_path):
            file_path = os.path.join(self.checkers_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
