import shutil
from pathlib import Path


def create_folder(output_path: str):
    Path(output_path).mkdir(exist_ok=True)
    print(f'{"=" * 5} Creation of {output_path} done {"=" * 5}')


def delete_folder(output_path: str):
    shutil.rmtree(Path(output_path))
    print(f'{"=" * 5} Deletion of {output_path} done {"=" * 5}')
