import demoqa_tests
import os
from pathlib import Path


# получение абсолютного пути к файлу
def get_abspath(path):
    file_path = str(Path(demoqa_tests.__file__).parent.parent.joinpath(f'tests_data/{path}'))
    return os.path.abspath(file_path)