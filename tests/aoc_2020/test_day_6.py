import pytest

from src.aoc_2020 import day_6

EXAMPLE_INPUT = """\
abc

a
b
c

ab
ac

a
a
a
a

b
"""

@pytest.fixture
def example_file_path(tmp_path):
    path = tmp_path / "day_6_test_input.txt"
    path.write_text(EXAMPLE_INPUT)
    return path

def test_get_sum_of_any_yes_from_file(example_file_path):
    result = day_6.get_sum_of_any_yes_from_file(example_file_path)
    assert result == 11

def test_get_sum_of_all_yes_from_file(example_file_path):
    result = day_6.get_sum_of_all_yes_from_file(example_file_path)
    assert result == 6

def test_get_sum_of_any_yes_from_file_challenge():
    result = day_6.get_sum_of_any_yes_from_file(day_6.INPUT_FILE_PATH)
    assert result == 7120

def test_get_sum_of_all_yes_from_file_challenge():
    result = day_6.get_sum_of_all_yes_from_file(day_6.INPUT_FILE_PATH)
    assert result == 3570
    