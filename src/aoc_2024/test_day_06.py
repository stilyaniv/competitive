from aoc_2024.day_06 import part_1, part_2, EXAMPLE, INPUT_FILE_PATH
import io


def test_part_1_example():
    with io.StringIO(EXAMPLE) as f:
        assert part_1(f) == 41


def test_part_1_full():
    with open(INPUT_FILE_PATH) as f:
        assert part_1(f) == 5551


def test_part_2_example():
    with io.StringIO(EXAMPLE) as f:
        assert part_2(f) == 6


def test_part_2_full():
    with open(INPUT_FILE_PATH) as f:
        assert part_2(f) == 1939
