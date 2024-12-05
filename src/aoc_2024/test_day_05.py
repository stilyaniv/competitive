from aoc_2024.day_05 import part_1, part_2, EXAMPLE, INPUT_FILE_PATH
import io


# TODO create test for sorting check
invalid_lines = [
    ["75", "97", "47", "61", "53"],  # 97,75,47,61,53
    ["75", "97", "53", "61", "47"],  # 97,75,47,61,53
    ["53", "97", "75", "61", "47"],  # 97,75,47,61,53
    ["53", "47", "75", "61", "97"],  # 97,75,47,61,53
    ["61", "13", "29"],  # 61,29,13
    ["97", "13", "75", "29", "47"],  # 97,75,47,29,13
]


def test_bigger_than():
    pass


def test_part_1_example():
    with io.StringIO(EXAMPLE) as f:
        assert part_1(f) == 143


def test_part_1_full():
    with open(INPUT_FILE_PATH) as f:
        assert part_1(f) == 7307


def test_part_2_example():
    with io.StringIO(EXAMPLE) as f:
        assert part_2(f) == 123


def test_part_2_full():
    with open(INPUT_FILE_PATH) as f:
        assert part_2(f) == 4713
