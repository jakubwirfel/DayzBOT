import os


class FileUtils:
    def __init__(self):
        self.path = r'C:\tmp\DayzBot'

    def create_data_folder(self) -> None:
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def remove_files_when_3(self) -> None:
        list_of_files = os.listdir(self.path)
        full_path = [self.path.format(x) for x in list_of_files]
        if len(list_of_files) == 3:
            oldest_file = min(full_path, key=os.path.getctime)
            os.remove(oldest_file)
