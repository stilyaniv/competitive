"""
https://adventofcode.com/
"""  # TODO link to problem
import io
from pathlib import Path

EXAMPLE = """\

"""

INPUT_FILE_PATH = f"{Path(__file__).parent / Path(__file__).stem}.txt"

PART1_EXAMPLE_OUTPUT = None
PART2_EXAMPLE_OUTPUT = None


def part_1(file):
    for line in file:
        pass

    return


def part_2(file):
    for line in file:
        pass

    return


if __name__ == "__main__":
    with io.StringIO(EXAMPLE) as f:
        print(f"{part_1(f)} == {PART1_EXAMPLE_OUTPUT}?")

    with open(INPUT_FILE_PATH) as f:
        print(part_1(f))

    with io.StringIO(EXAMPLE) as f:
        print(f"{part_2(f)} == {PART2_EXAMPLE_OUTPUT}?")

    with open(INPUT_FILE_PATH) as f:
        print(part_2(f))
