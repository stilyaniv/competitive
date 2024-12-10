"""
https://adventofcode.com/
"""  # TODO link to problem

import io
from pathlib import Path

EXAMPLE = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

INPUT_FILE_PATH = f"{Path(__file__).parent / Path(__file__).stem}.txt"

PART1_EXAMPLE_OUTPUT = 36
PART2_EXAMPLE_OUTPUT = None

from typing import Dict, List


def print_grid(grid: List[List], locations: Dict[str, List], empty_cell=".") -> None:
    for char, pairs in locations.items():
        for pair in pairs:
            x, y = pair
            if grid[y][x] == empty_cell:
                grid[y][x] = char
    new_grid = "\n".join(["".join([c for c in row]) for row in grid])
    print(new_grid)


def create_grid(file):
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


TRAIL = [str(n) for n in range(10)]


# EXAMPLE = """\
# 89010123456789
# """


def traverse(grid, x_len, y_len, x, y, trail_idx, ends):
    if not (0 <= x < x_len and 0 <= y < y_len):
        return
    if trail_idx != 0 and int(grid[y][x]) != trail_idx:
        return
    if trail_idx == 9:
        ends += [(x, y)]
        return

    trail_idx += 1

    left = traverse(grid, x_len, y_len, x - 1, y, trail_idx, ends)
    right = traverse(grid, x_len, y_len, x + 1, y, trail_idx, ends)
    up = traverse(grid, x_len, y_len, x, y - 1, trail_idx, ends)
    down = traverse(grid, x_len, y_len, x, y + 1, trail_idx, ends)

    # return left + right + up + down
    return ends


def part_1(file):
    grid, x_len, y_len, special_chars = create_grid(file)
    grid_f = "\n".join(["".join([c for c in row]) for row in grid])
    # print(grid_f)
    scores = {}
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != "0":
                continue
            print(x, y)
            ends = traverse(grid, x_len, y_len, x, y, 0, [])
            # scores[(x, y)] = sum(1 if s else 0 for s in score)
            scores[(x, y)] = len(set(ends))

    print(scores)
    return sum(scores.values())

    # visited = []
    # trail_idx = 1
    # x1, y1 = x + 1, y
    # while True:
    #     if not (0 <= x1 < x_len and 0 <= y1 < y_len):
    #         break
    #     else:
    #         visited.append((x1, y1))
    #     if int(grid[y1][x1]) == trail_idx:
    #         if trail_idx == 9:
    #             trail_idx = 1
    #             x1, y1 = x, y
    #         else:
    #             trail_idx += 1
    #             x, y = x + 1, y
    #     elif int(grid[y1][x1]) > trail_idx:
    #         break


if __name__ == "__main__":
    with io.StringIO(EXAMPLE) as f:
        print(f"{part_1(f)} == {PART1_EXAMPLE_OUTPUT}?")

    with open(INPUT_FILE_PATH) as f:
        print(part_1(f))

    # with io.StringIO(EXAMPLE) as f:
    #     print(f"{part_2(f)} == {PART2_EXAMPLE_OUTPUT}?")

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_2(f))

    # 6287341702001 too high
    # 6287404501347 too high
    # 6287527318218
