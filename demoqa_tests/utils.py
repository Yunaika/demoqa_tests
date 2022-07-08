from enum import Enum

import demoqa_tests
import os
from pathlib import Path


class Months(Enum):
    January = 0
    February = 1
    March = 2
    April = 3
    May = 4
    June = 5
    July = 6
    August = 7
    September = 8
    October = 9
    November = 10
    December = 11


def get_abspath(path):
    """
    получение абсолютного пути к файлу
    """
    file_path = str(Path(demoqa_tests.__file__).parent.parent.joinpath(f'tests_data/{path}'))
    return os.path.abspath(file_path)
