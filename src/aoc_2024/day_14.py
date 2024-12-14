"""
https://adventofcode.com/
"""  # TODO link to problem
import io
import re
from pathlib import Path

EXAMPLE = """\
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""

INPUT_FILE_PATH = f"{Path(__file__).parent / Path(__file__).stem}.txt"

PART1_EXAMPLE_OUTPUT = 12
PART2_EXAMPLE_OUTPUT = None


X_Y_PATTERN = r"p=(\d*),(\d*) v=(-?\d*),(-?\d*)"


def part_1(file, x_size, y_size):
    # x_size, y_size = 11, 7
    x_mid = x_size // 2
    y_mid = y_size // 2
    # robots = []
    # grid = [[]]
    q = {1: 0, 2: 0, 3: 0, 4: 0}
    for line in file:
        x, y, xv, yv = [int(n) for n in re.search(X_Y_PATTERN, line.strip()).groups()]
        # robots.append(tuple(int(n) for n in (x, y, xv, yv)))
        # x, y, xv, yv = int(x), int(x),
        # x, y, xv, yv = 2, 4, 2, -3
        for s in range(100):
            x, y = (x+xv) % x_size, (y+yv) % y_size
        print(x, y)
        if x < x_mid and y < y_mid:
            q[1] += 1
        elif x > x_mid and y < y_mid:
            q[2] += 1
        elif x < x_mid and y > y_mid:
            q[3] += 1
        elif x > x_mid and y > y_mid:
            q[4] += 1
    return q[1] * q[2] * q[3] * q[4]


def part_2(file, x_size, y_size):
    for line in file:
        pass

    return


if __name__ == "__main__":
    with io.StringIO(EXAMPLE) as f:
        print(f"{part_1(f, 11, 7)} == {PART1_EXAMPLE_OUTPUT}?")

    with open(INPUT_FILE_PATH) as f:
        print(part_1(f, 101, 103))

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_2(f, 101, 103))
