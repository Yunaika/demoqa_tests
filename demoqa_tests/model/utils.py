from enum import Enum

import demoqa_tests
import os
from pathlib import Path


class Months(Enum):
    Jan = 0
    Feb = 1
    Mar = 2
    Apr = 3
    May = 4
    Jun = 5
    Jul = 6
    Aug = 7
    Sep = 8
    Oct = 9
    Nov = 10
    Dec = 11


def get_abspath(path):
    """
    получение абсолютного пути к файлу
    """
    file_path = str(Path(demoqa_tests.__file__).parent.parent.joinpath(f'tests_data/{path}'))
    return os.path.abspath(file_path)
