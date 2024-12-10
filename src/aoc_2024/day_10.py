"""
https://adventofcode.com/
"""  # TODO link to problem

import io
from pathlib import Path
from typing import Dict, List

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
PART1_OUTPUT = 510
PART2_EXAMPLE_OUTPUT = 81
PART2_OUTPUT = 1058


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


def traverse(grid, x_len, y_len, x, y, trail_idx, ends) -> List:
    if not (0 <= x < x_len and 0 <= y < y_len):
        return []
    if trail_idx != 0 and int(grid[y][x]) != trail_idx:
        return []
    if trail_idx == 9:
        ends += [(x, y)]
        return ends

    trail_idx += 1

    left = traverse(grid, x_len, y_len, x - 1, y, trail_idx, ends)
    right = traverse(grid, x_len, y_len, x + 1, y, trail_idx, ends)
    up = traverse(grid, x_len, y_len, x, y - 1, trail_idx, ends)
    down = traverse(grid, x_len, y_len, x, y + 1, trail_idx, ends)

    return ends


def part_1(file):
    grid, x_len, y_len, _ = create_grid(file)
    scores = {}
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != "0":
                continue
            ends = traverse(grid, x_len, y_len, x, y, 0, [])
            scores[(x, y)] = len(set(ends))

    return sum(scores.values())


# TODO refactor p1 and 2 are the same, unique 9s vs unique entire paths
def part_2(file):
    grid, x_len, y_len, _ = create_grid(file)
    scores = {}
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != "0":
                continue
            ends = traverse(grid, x_len, y_len, x, y, 0, [])
            scores[(x, y)] = len(ends)

    return sum(scores.values())


if __name__ == "__main__":
    with io.StringIO(EXAMPLE) as f:
        print(f"{part_1(f)} == {PART1_EXAMPLE_OUTPUT}?")

    with open(INPUT_FILE_PATH) as f:
        print(part_1(f))

    with io.StringIO(EXAMPLE) as f:
        print(f"{part_2(f)} == {PART2_EXAMPLE_OUTPUT}?")

    with open(INPUT_FILE_PATH) as f:
        print(part_2(f))
