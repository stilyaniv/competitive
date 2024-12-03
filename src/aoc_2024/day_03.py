"""
https://adventofcode.com/2024/day/3
"""
import io
import re

EXAMPLE_1 = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

EXAMPLE_2 = """\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

INPUT_FILE_PATH = r"src/aoc_2024/day_03.txt"

PATTERN_MUL = r"mul\((\d*,\d*)\)"
PATTERN_DO = r"(do\(\))"
PATTERN_DONT = r"(don't\(\))"
PATTERN_ALL = re.compile("|".join([PATTERN_MUL, PATTERN_DO, PATTERN_DONT]))


def part_1(file):
    total = 0
    data = file.read()
    for m in re.findall(re.compile(PATTERN_MUL), data):
        a, b = m.split(",")
        total += int(a) * int(b)

    return total


def part_2(file):
    total = 0
    data = file.read()
    enabled = True
    for m in re.findall(PATTERN_ALL, data):
        pair, do, dont = m
        if do:
            enabled = True
        elif dont:
            enabled = False
        elif pair and enabled:
            a, b = pair.split(",")
            total += int(a) * int(b)

    return total


if __name__ == "__main__":
    with io.StringIO(EXAMPLE_1) as f:
        print(part_1(f))

    with open(INPUT_FILE_PATH) as f:
        print(part_1(f))

    with io.StringIO(EXAMPLE_2) as f:
        print(part_2(f))

    with open(INPUT_FILE_PATH) as f:
        print(part_2(f))
