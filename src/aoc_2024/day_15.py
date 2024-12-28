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


def read_grid_moves(file):
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
    # grid_str = "\n".join(["".join([str(x) if x else BLANK for x in row]) for row in grid])
    # print(grid_str)
    # print(moves)
    x, y = special_chars['@'][0]
    print(f"Starting position: {special_chars['@']}")
    print("\n".join(["".join([str(x) for x in row]) for row in grid]))

    return x, y, grid, moves


@timing
def part_1(file):
    x, y, grid, moves = read_grid_moves(file)

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

v
"""

EXAMPLE_PART_2_SIMPLE = """\
####################
##..[]............##
##...[]...........##
##....[]..........##
##.....@..........##
##....[]..........##
##................##
##...[][].........##
##..[]............##
##................##
####################

v
"""


def find_space(x, y, xc, yc, grid):
    pass


def walk(x, y, xc, yc, grid):
    can_move = False
    xn, yn = (x + xc, y + yc)
    if grid[yn][xn] == BLANK:
        grid[yn][xn] = grid[y][x]
        grid[y][x] = BLANK
        x, y = xn, yn
        can_move = True
    elif grid[yn][xn] == ']' or grid[yn][xn] == '[':
        # move left or right
        if xc != 0:
            xnn, ynn = (xn + xc, yn + yc)
            print(grid[yn][xn], grid[ynn][xnn])
            if grid[ynn][xnn] != '#':
                xnn, ynn, can_move = walk(xnn, ynn, xc, yc, grid)
                if can_move:
                    xn, yn, can_move = walk(xn, yn, xc, yc, grid)
                    x, y, can_move = walk(x, y, xc, yc, grid)
        if yc != 0:
            # xnn, ynn = (xn + xc, yn + yc)
            # print(grid[yn][xn], grid[ynn][xnn])
            # if grid[ynn][xnn] != '#':
            staging = [(x, y)]
            current_level = []
            level = 1
            for x, y in staging:
                xn, yn = (x + xc, y + yc)
                if grid[yn][xn] == ']':
                    x_l, y_l = xn-1, yn
                    x_r, y_r = xn, yn
                elif grid[yn][xn] == '[':
                    x_l, y_l = xn, yn
                    x_r, y_r = xn+1, yn
                # TODO need to detect . at this point otherwise x_l, x_r etc
                #      stay the same and it keep reinserting to current level
                current_level.extend([(x_l, y_l), (x_r, y_r)])
                if len(current_level) == 2 ** level:
                    if all(grid[y][x] == BLANK for x, y in current_level):
                        while staging:
                            can_move = True
                            xn, yn = (x + xc, y + yc)
                            grid[yn][xn] = grid[y][x]
                            grid[y][x] = BLANK
                            # x, y = xn, yn
                    else:
                        staging.extend(current_level)
                        current_level = []
                        level += 1
                else:
                    current_level.extend([(x_l, y_l), (x_r, y_r)])

                print(grid[y_l][x_l], grid[y_r][x_r])
            # can_move = find_space(x_object_left, y_object_left, xc, yc, grid)
            # can_move = find_space(x_object_right, y_object_right, xc, yc, grid)

            # xnn, ynn, can_move = walk(xnn, ynn, xc, yc, grid)
            # if can_move:
            #     xn, yn, can_move = walk(xn, yn, xc, yc, grid)
            #     x, y, can_move = walk(x, y, xc, yc, grid)

    return x, y, can_move


def part_2(file):
    x, y, grid, moves = read_grid_moves(file)
    for move in moves:
        if move == "<":
            xc, yc = (-1, 0)
        elif move == ">":
            xc, yc = (1, 0)
        elif move == "^":
            xc, yc = (0, -1)
        elif move == "v":
            xc, yc = (0, 1)

        x, y, can_move = walk(x, y, xc, yc, grid)
        if can_move:
            print(f"Move {move} resulted in:")
        else:
            print(f"Move {move} skipped.")

        print("\n".join(["".join([str(x) for x in row]) for row in grid]))
        sleep(0.5)

    gps_sums = 0
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if grid[y][x] == "O":
                gps_sums += x + 100*y
    return gps_sums


if __name__ == "__main__":
    # with io.StringIO(EXAMPLE) as f:
    #     print(f"{part_1(f)} == {PART1_EXAMPLE_OUTPUT}?")

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_1(f))

    with io.StringIO(EXAMPLE_PART_2_SIMPLE) as f:
        part_2(f)

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_2(f))
