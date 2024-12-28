import io

from aoc_2024.day_12 import (EXAMPLE, INPUT_FILE_PATH, PART1_EXAMPLE_OUTPUT,
                             PART2_EXAMPLE_OUTPUT, part_1, part_2)


def test_part_1_example():
    with io.StringIO(EXAMPLE) as f:
        assert part_1(f) == PART1_EXAMPLE_OUTPUT


def test_part_1_full():
    with open(INPUT_FILE_PATH) as f:
        assert part_1(f) == 1489582


def test_part_2_example():
    with io.StringIO(EXAMPLE) as f:
        assert part_2(f) == PART2_EXAMPLE_OUTPUT


def test_part_2_full():
    with open(INPUT_FILE_PATH) as f:
        assert part_2(f) is None
