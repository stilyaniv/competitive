import io

from aoc_2024.day_09 import (EXAMPLE, INPUT_FILE_PATH, PART1_EXAMPLE_OUTPUT,
                             PART2_EXAMPLE_OUTPUT, part_1, part_2)


def test_part_1_example():
    with io.StringIO(EXAMPLE) as f:
        assert part_1(f) == PART1_EXAMPLE_OUTPUT


def test_part_1_full():
    with open(INPUT_FILE_PATH) as f:
        assert part_1(f) == 6262891638328


def test_part_2_example():
    with io.StringIO(EXAMPLE) as f:
        assert part_2(f) == PART2_EXAMPLE_OUTPUT


def test_part_2_full():
    with open(INPUT_FILE_PATH) as f:
        assert part_2(f) is None


def test_part_2_edge_cases():
    # Test Case 1: No movement possible
    assert part_2(io.StringIO("11")) == "0."
    # Test Case 2: Multiple gaps
    # assert part_2(io.StringIO("1212")) == "1122"
    # Test Case 3: Already optimal
    # assert part_2(io.StringIO("2020")) == "00.."
    # Test Case 4: Complex movement required
    # assert part_2(io.StringIO("102030")) == "302010"
    # Test Case 5: Edge file movement
    assert part_2(io.StringIO("0121")) == "1102"
