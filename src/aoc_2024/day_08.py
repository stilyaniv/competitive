"""
https://adventofcode.com/
"""  # TODO link to problem
from enum import unique
import io
from pathlib import Path
from pprint import pprint
from typing import Dict, List

EXAMPLE = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

PART_1_OUTPUT = 14
PART_2_OUTPUT = 34

INPUT_FILE_PATH = f"{Path(__file__).parent / Path(__file__).stem}.txt"


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


# TODO refactor to use the part2 function with step=1
def part_1(file):
    grid, x_len, y_len, special_chars = create_grid(file)
    unique_placements = set()
    pprint(special_chars)
    antis = {}
    special_chars = {k: special_chars[k] for k in special_chars if k != "."}
    for char, pairs in special_chars.items():
        for i, pair1 in enumerate(pairs):
            for j in range(i + 1, len(pairs)):
                x1, y1 = pair1
                x2, y2 = pairs[j]
                x_d = x2 - x1
                y_d = y2 - y1
                anti_nodes = [(x1 - x_d, y1 - y_d), (x2 + x_d, y2 + y_d)]
                if char in antis:
                    antis[char] += anti_nodes
                else:
                    antis[char] = anti_nodes
                for anti_node in anti_nodes:
                    if 0 <= anti_node[0] < x_len and 0 <= anti_node[1] < y_len:
                        unique_placements.update({anti_node})

    print(unique_placements)
    return len(unique_placements)


def part_2(file):
    grid, x_len, y_len, special_chars = create_grid(file)
    unique_anti_nodes = set()
    pprint(special_chars)
    anti_nodes = []
    special_chars = {k: special_chars[k] for k in special_chars if k != "."}
    for char, pairs in special_chars.items():
        for i in range(len(pairs)):
            for j in range(i + 1, len(pairs)):
                x1, y1 = pairs[i]
                x2, y2 = pairs[j]
                x_d = x2 - x1
                y_d = y2 - y1
                anti_nodes.extend([(x1, y1), (x2, y2)])
                steps = 1
                while True:
                    new_x, new_y = (x2 + steps * x_d, y2 + steps * y_d)
                    if 0 <= new_x < x_len and 0 <= new_y < y_len:
                        anti_nodes.append((new_x, new_y))
                        steps += 1
                    else:
                        break
                steps = 1
                while True:
                    new_x, new_y = (x2 - steps * x_d, y2 - steps * y_d)
                    if 0 <= new_x < x_len and 0 <= new_y < y_len:
                        anti_nodes.append((new_x, new_y))
                        steps += 1
                    else:
                        break
    unique_anti_nodes = set(anti_nodes)

    # visualise
    # locations = special_chars
    # locations.update({"#": unique_anti_nodes})
    # print_grid(grid, locations)

    return len(unique_anti_nodes)


if __name__ == "__main__":
    with io.StringIO(EXAMPLE) as f:
        print(f"{part_1(f)} == {PART_1_OUTPUT}?")

    with open(INPUT_FILE_PATH) as f:
        print(part_1(f))  # 301

    with io.StringIO(EXAMPLE) as f:
        print(f"{part_2(f)} == {PART_2_OUTPUT}?")

    with open(INPUT_FILE_PATH) as f:
        print(part_2(f))  # 1019
