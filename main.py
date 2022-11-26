from helpers.threads_helper import ThreadHelper
from utils.file_utils import FileUtils
from verifiers import Verifiers

if __name__ == "__main__":
    FileUtils().create_data_folder()
    Verifiers()
    ThreadHelper().player_executor()
