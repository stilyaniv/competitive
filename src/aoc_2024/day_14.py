"""
https://adventofcode.com/
"""  # TODO link to problem
import io
import re
from pathlib import Path
from time import sleep

import pandas as pd

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

# TODO write test for state after 100 seconds
# ......2..1.
# ...........
# 1..........
# .11........
# .....1.....
# ...12......
# .1....1....


INPUT_FILE_PATH = f"{Path(__file__).parent / Path(__file__).stem}.txt"

PART1_EXAMPLE_OUTPUT = 12
PART2_EXAMPLE_OUTPUT = 222208000
PART2_OUTPUT = 7623

X_Y_PATTERN = r"p=(\d*),(\d*) v=(-?\d*),(-?\d*)"

BLANK = " "
BLOCK = '█'


def part_1(file, x_size, y_size):
    x_mid = x_size // 2
    y_mid = y_size // 2
    q = {1: 0, 2: 0, 3: 0, 4: 0}
    for line in file:
        x, y, xv, yv = [int(n) for n in re.search(X_Y_PATTERN, line.strip()).groups()]
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


def draw_frame(x_size, y_size, robots, sec):
    grid = [[0 for x in range(x_size)] for y in range(y_size)]
    for i, robot in enumerate(robots):
        x, y, xv, yv = robot
        x, y = (x+sec*xv) % x_size, (y+sec*yv) % y_size
        grid[y][x] += 1
    grid_str = "\n".join(["".join([str(x) if x else BLANK for x in row]) for row in grid])
    print(grid_str)


def part_2(file, x_size, y_size):
    x_mid = x_size // 2
    y_mid = y_size // 2
    robots = []
    s = 0
    grid = [[0 for x in range(x_size)] for y in range(y_size)]
    for line in file:
        x, y, xv, yv = [int(n) for n in re.search(X_Y_PATTERN, line.strip()).groups()]
        robots.append((x, y, xv, yv))
        grid[y][x] += 1
        grid_str = "\n".join(["".join([str(c) if c else BLANK for c in row]) for row in grid])
    print(f"{s=}")
    print(grid_str)

    draw_frame(x_size, y_size, robots, 7623)

    data = []
    while s < 10 ** 4:
        s += 1
        q1, q2, q3, q4 = 0, 0, 0, 0
        for i, robot in enumerate(robots):
            x, y, xv, yv = robot
            x, y = (x+s*xv) % x_size, (y+s*yv) % y_size
            if x < x_mid and y < y_mid:
                q1 += 1
            elif x > x_mid and y < y_mid:
                q2 += 1
            elif x < x_mid and y > y_mid:
                q3 += 1
            elif x > x_mid and y > y_mid:
                q4 += 1
        score = q1*q2*q3*q4
        # print(f"{s=} {q1} {q2} {q3} {q4} = {score}")
        data.append([s, q1, q2, q3, q4, score])
    df = pd.DataFrame(data=data, columns=['sec', 1, 2, 3, 4, "score"])
    outlier = df.sort_values(['score'], ascending=True).head(1)
    sec = int(outlier['sec'].iloc[0])
    draw_frame(x_size, y_size, robots, sec)

    return outlier['score']


if __name__ == "__main__":
    # with io.StringIO(EXAMPLE) as f:
    #     print(f"{part_1(f, 11, 7)} == {PART1_EXAMPLE_OUTPUT}?")

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_1(f, 101, 103))

    # with io.StringIO(EXAMPLE) as f:
    #     part_2(f, 11, 7)

    with open(INPUT_FILE_PATH) as f:
        print(part_2(f, 101, 103))
