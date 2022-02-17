import shutil
import os


def create_folder(output_path: str):
    os.mkdir(output_path)
    print(f'{"=" * 5} + "Creation of {output_path} done" + {"=" * 5}')


def delete_folder(output_path: str):
    shutil.rmtree(os.path.join(output_path))
    print(f'{"=" * 5} + "Deletion of {output_path} done" + {"=" * 5}')
