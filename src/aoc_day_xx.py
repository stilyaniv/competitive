"""
https://adventofcode.com/
"""  # TODO link to problem
import io

EXAMPLE = """\

"""  # TODO small size example from problem

# TODO path to challenge input, assumes template was copied to correct directory
INPUT_FILE_PATH = r"src/aoc_20xx/day_xx.txt"


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

    with io.StringIO(EXAMPLE) as f:
        print(part_2(f))

    with open(INPUT_FILE_PATH) as f:
        print(part_1(f))

    with open(INPUT_FILE_PATH) as f:
        print(part_2(f))
