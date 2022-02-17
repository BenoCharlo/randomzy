import shutil
from pathlib import Path

from . import settings


def create_folder(folder_name: str = settings.TEMP_FOLDER):
    Path(folder_name).mkdir(exist_ok=True)
    return f'"=" * 5 + "Creation of {folder_name} done" + "=" * 5'


def delete_folder(folder_name: str = settings.TEMP_FOLDER):
    shutil.rmtree(Path(folder_name))
    return f'"=" * 5 + "Deletion of {folder_name} done" + "=" * 5'
