import shutil
import os

from . import settings


def create_folder(folder_name: str = settings.TEMP_FOLDER):
    os.makedirs(folder_name, exist_ok=True)
    return f'"=" * 5 + "Creation of {folder_name} done" + "=" * 5'


def delete_folder(folder_name: str = settings.TEMP_FOLDER):
    shutil.rmtree(os.path.join(folder_name))
    return f'"=" * 5 + "Deletion of {folder_name} done" + "=" * 5'
