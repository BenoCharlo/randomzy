import shutil
from pathlib import Path


def create_folder(folder_name: str = "temp"):
    return Path(folder_name).mkdir(exist_ok=True)


def delete_folder(folder_name: str = "temp"):
    return shutil.rmtree(Path(folder_name))
