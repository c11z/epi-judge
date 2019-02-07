from test_framework import generic_test
from typing import List

def convert_base(num_as_string: str, b1: int, b2: int):
    hex: List[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    is_neg = num_as_string
    return ''


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
