"""
https://adventofcode.com/
"""  # TODO link to problem
import io
import re
from functools import wraps
from pathlib import Path
from time import sleep, time

import pandas as pd

EXAMPLE_SMALL = """\
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
"""


EXAMPLE = """\
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

EXAMPLE_PART_2 = """\
####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]@.....[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""


INPUT_FILE_PATH = f"{Path(__file__).parent / Path(__file__).stem}.txt"

PART1_EXAMPLE_SMALL_OUTPUT = 2028
PART1_EXAMPLE_OUTPUT = 10092
PART1_OUTPUT = 1406628
PART2_EXAMPLE_OUTPUT = None
PART2_OUTPUT = None

BLANK = "."
BLOCK = '█'


def create_grid(file):
    # TODO modify so it ignores blank line and stops reading
    grid = []
    special_chars = {}
    x_len, y_len = 0, 0
    for y, line in enumerate(file):
        y_len += 1
        row = []
        for x, char in enumerate(line.strip()):
            row.append(char)
            if char in special_chars:
                special_chars[char] += [(x, y)]
            else:
                special_chars[char] = [(x, y)]
        grid.append(row)

    x_len, y_len = x + 1, y + 1
    return grid, x_len, y_len, special_chars


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' %
              (f.__name__, args, kw, te - ts))
        return result
    return wrap


@timing
def part_1(file):
    grid = []
    moves = []
    x, y = 0, 0
    special_chars = {}
    for line in file:
        if line == '\n':
            continue
        elif line.startswith("#"):
            row = []
            for x, char in enumerate(line.strip()):
                row.append(char)
                if char in special_chars:
                    special_chars[char] += [(x, y)]
                else:
                    special_chars[char] = [(x, y)]
            y += 1
            grid.append(row)
        else:
            moves.extend([c for c in line.strip()])
    grid_str = "\n".join(["".join([str(x) if x else BLANK for x in row]) for row in grid])
    # print(grid_str)
    # print(moves)
    x, y = special_chars['@'][0]
    print(f"Starting position: {special_chars['@']}")

    for move in moves:
        if move == "<":
            xc, yc = (-1, 0)
        elif move == ">":
            xc, yc = (1, 0)
        elif move == "^":
            xc, yc = (0, -1)
        elif move == "v":
            xc, yc = (0, 1)

        xn, yn = (x + xc, y + yc)
        if grid[yn][xn] == BLANK:
            grid[yn][xn] = "@"
            grid[y][x] = BLANK
            x, y = xn, yn
        elif grid[yn][xn] == "O":
            xnn, ynn = xn, yn
            while grid[ynn][xnn] == "O":
                xnn, ynn = (xnn + xc, ynn + yc)
            if grid[ynn][xnn] == BLANK:
                grid[ynn][xnn] = "O"
                grid[yn][xn] = "@"
                grid[y][x] = BLANK
                x, y = xn, yn
        # print(move)
        # print("\n".join(["".join([str(x) for x in row]) for row in grid]))

    gps_sums = 0
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if grid[y][x] == "O":
                gps_sums += x + 100*y
    return gps_sums


def part_2(file):
    pass


if __name__ == "__main__":
    # with io.StringIO(EXAMPLE) as f:
    #     print(f"{part_1(f)} == {PART1_EXAMPLE_OUTPUT}?")

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_1(f))

    with io.StringIO(EXAMPLE) as f:
        part_2(f)

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_2(f))
