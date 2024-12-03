from aoc_2024.day_03 import part_1, part_2, EXAMPLE_1, EXAMPLE_2, INPUT_FILE_PATH
import io


def test_part_1_example():
    with io.StringIO(EXAMPLE_1) as f:
        assert part_1(f) == 161


def test_part_1_full():
    with open(INPUT_FILE_PATH) as f:
        assert part_1(f) == 183380722


def test_part_2_example():
    with io.StringIO(EXAMPLE_2) as f:
        assert part_2(f) == 48


def test_part_2_full():
    with open(INPUT_FILE_PATH) as f:
        assert part_2(f) == 82733683
