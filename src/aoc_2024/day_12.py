"""
https://adventofcode.com/
"""  # TODO link to problem
import io
from pathlib import Path
from pprint import pprint
from typing import List

EXAMPLE = """\
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""


INPUT_FILE_PATH = f"{Path(__file__).parent / Path(__file__).stem}.txt"

PART1_EXAMPLE_OUTPUT = 1930
PART2_EXAMPLE_OUTPUT = 1206


class Square:
    def __init__(self, x, y, grid) -> None:
        self.x = x
        self.y = y
        self.E = grid[y][x-1]
        self.W = grid[y][x+1]
        self.N = grid[y-1][x]
        self.S = grid[y+1][x]
        self.garden = None

    def perim(self):
        neighbours = [self.E, self.W, self.N, self.S]
        return sum(1 if s else 0 for s in neighbours)

    def get_neighbour_gardens(self):
        return


class Garden:
    def __init__(self):
        self.squares = []

    def add(self, square):
        self.squares.append(square)


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


def coordinates_to_grid(coordinates):
    for x, y in coordinates:
        pass


BLANK = " "
BLOCK = '█'


def draw_frame(x_size, y_size, positions):
    grid = [[0 for x in range(x_size)] for y in range(y_size)]
    for i, (x, y) in enumerate(positions):
        # x, y = positions
        grid[y][x] = BLOCK
    grid_str = "\n".join(["".join([BLOCK if x else BLANK for x in row]) for row in grid])
    print(grid_str)


def traverse_2(grid, x_len, y_len, x, y, square, visited, garden):
    if (x, y) in visited and grid[y][x] == square:
        return []
    if (x, y) in visited and grid[y][x] != square:
        return [(x, y)]
    if not (0 <= x < x_len and 0 <= y < y_len):
        return [(x, y)]
    if grid[y][x] != square:
        return [(x, y)]

    garden.extend([(x, y)])
    visited.extend([(x, y)])

    left = traverse_2(grid, x_len, y_len, x - 1, y, square, visited, garden)
    right = traverse_2(grid, x_len, y_len, x + 1, y, square, visited, garden)
    up = traverse_2(grid, x_len, y_len, x, y - 1, square, visited, garden)
    down = traverse_2(grid, x_len, y_len, x, y + 1, square, visited, garden)

    perim = left + right + up + down
    return perim


def part_2(file):
    grid, x_len, y_len, squares = create_grid(file)

    total_price = 0
    visited = []
    for y in range(y_len):
        for x in range(x_len):
            square = grid[y][x]
            garden = []
            perim = traverse_2(grid, x_len, y_len, x, y, square, visited, garden)
            # draw_frame(x_len, y_len, perim)
            perims = sorted(perim, key=lambda t: (t[0], t[1]))
            # TODO perims - remove from perims if two nodes differ by exactly 1 unit of x or 1 unit of y
            price = len(garden) * len(perim)
            total_price += price
            if garden or perim:
                print(f"{square}: {len(garden)} * {perim} = {price}")
    return total_price


if __name__ == "__main__":
    # with io.StringIO(EXAMPLE) as f:
    #     print(f"{part_1(f)} == {PART1_EXAMPLE_OUTPUT}?")

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_1(f))

    with io.StringIO(EXAMPLE) as f:
        print(f"{part_2(f)} == {PART2_EXAMPLE_OUTPUT}?")

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_2(f))
