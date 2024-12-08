"""
https://adventofcode.com/
"""  # TODO link to problem
import io
from pathlib import Path

EXAMPLE = """\

"""  # TODO small size example from problem

INPUT_FILE_PATH = f"{Path(__file__).parent / Path(__file__).stem}.txt"


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
        print(part_1(f))

    with open(INPUT_FILE_PATH) as f:
        print(part_1(f))

    # with io.StringIO(EXAMPLE) as f:
    #     print(part_2(f))

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_2(f))
