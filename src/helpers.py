import shutil
from pathlib import Path


def create_folder(folder_name: str = "temp"):
    Path(folder_name).mkdir(exist_ok=True)
    return f'"=" * 5 + "Creation of {folder_name} done" + "=" * 5'


def delete_folder(folder_name: str = "temp"):
    shutil.rmtree(Path(folder_name))
    return f'"=" * 5 + "Deletion of {folder_name} done" + "=" * 5'
