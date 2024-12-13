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

PART1_EXAMPLE_OUTPUT = None
PART2_EXAMPLE_OUTPUT = None


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


def traverse(grid, x_len, y_len, x, y, square, visited, garden):
    # area, perim = 0, 0
    if (x, y) in visited and grid[y][x] == square:
        return 0
    if (x, y) in visited and grid[y][x] != square:
        return 1
    if not (0 <= x < x_len and 0 <= y < y_len):
        # visited.extend([(x, y)])
        return 1
    if grid[y][x] != square:
        # return [(x, y)], 0, 1
        return 1
    if (x, y) not in visited and grid[y][x] == square:
        garden.extend([(x, y)])
        visited.extend([(x, y)])
        # return 0
    # left = grid[y][x-1]
    # right = grid[y][x+1]
    # up = grid[y-1][x]
    # down = grid[y+1][x]
    area = 0
    # perim = 0
    area += 1
    # if ()
    left = traverse(grid, x_len, y_len, x - 1, y, square, visited, garden)
    right = traverse(grid, x_len, y_len, x + 1, y, square, visited, garden)
    up = traverse(grid, x_len, y_len, x, y - 1, square, visited, garden)
    down = traverse(grid, x_len, y_len, x, y + 1, square, visited, garden)
    # loc = right[0]
    # visited.extend(loc)
    # area += right[1]
    # perim += right[2]

    # print(right)
    # print((x, y))
    # return visited, area, perim
    perim = left + right + up + down
    return perim


def part_1(file):
    grid, x_len, y_len, squares = create_grid(file)

    total_area, total_price = 0, 0
    visited = []
    for y in range(y_len):
        for x in range(x_len):
            # if (x, y) in not:
            #     continue
            # x, y = 2, 5
            square = grid[y][x]
            # square = grid[0][0]
            garden = []
            perim = traverse(grid, x_len, y_len, x, y, square, visited, garden)
            # break
            # if (x, y) not in gardens:
            #     gardens[(x, y)] = (area, perim)
            #     mapped_squares.extend(visited)

            # grid[y][x] = Square(x, y, grid)
            total_area += len(garden)
            price = len(garden) * perim
            total_price += price
            if garden or perim:
                print(f"{square}: {len(garden)} * {perim} = {price}")
    # pprint(set(visited))
    return total_price


class Square:

    def __init__(self, x, y, grid) -> None:
        self.x = x
        self.y = y
        self.E = grid[y][x-1]
        self.W = grid[y][x+1]
        self.N = grid[y-1][x]
        self.S = grid[y+1][x]
        self.garden = None
        # self.E = None
        # self.W = None
        # self.N = None
        # self.S = None

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


def part_1_objects(file):
    # if (x, y) in not :
    #     continue
    # square = grid[y][x]
    # left = grid[y][x-1]
    # right = grid[y][x+1]
    # up = grid[y-1][x]
    # down = grid[y+1][x]

    # visited, area, perim = traverse(grid, x_len, y_len, x, y, square)
    # if (x, y) not in gardens:
    #     gardens[(x, y)] = (area, perim)
    #     mapped_squares.extend(visited)

    # grid[y][x] = Square(x, y, grid)

    # pprint(gardens)
    return gardens


def part_1_left_to_right(file):
    """
    traverse left to right top to bottom
    doesn't work without extra changes as we create new gardens too early
    """
    grid, x_len, y_len, squares = create_grid(file)

    # mapped_squares = []
    squares = {}
    gardens = {}
    garden_index = 0
    for y in range(y_len):
        for x in range(x_len):
            if (x+1, y) in gardens and grid[y][x] == grid[y][x+1]:
                gardens[(x, y)] = gardens[(x+1, y)]
            elif (x-1, y) in gardens and grid[y][x] == grid[y][x-1]:
                gardens[(x, y)] = gardens[(x-1, y)]
            elif (x, y+1) in gardens and grid[y][x] == grid[y+1][x]:
                gardens[(x, y)] = gardens[(x, y+1)]
            elif (x, y-1) in gardens and grid[y][x] == grid[y-1][x]:
                gardens[(x, y)] = gardens[(x, y-1)]
            else:
                gardens[(x, y)] = garden_index
                # grid[y][x] = garden_index
                garden_index += 1
    for (x, y), garden_index in gardens.items():
        grid[y][x] = garden_index
    pprint(grid)
    new_grid = "\n".join([" ".join([f"{str(c):>2}" for c in row]) for row in grid])
    print(new_grid)

    # if (x, y) in not :
    #     continue
    # square = grid[y][x]
    # left = grid[y][x-1]
    # right = grid[y][x+1]
    # up = grid[y-1][x]
    # down = grid[y+1][x]

    # visited, area, perim = traverse(grid, x_len, y_len, x, y, square)
    # if (x, y) not in gardens:
    #     gardens[(x, y)] = (area, perim)
    #     mapped_squares.extend(visited)

    # grid[y][x] = Square(x, y, grid)

    # pprint(gardens)
    return gardens


def part_2(file):
    for line in file:
        pass

    return


if __name__ == "__main__":
    # with io.StringIO(EXAMPLE) as f:
    #     print(f"{part_1(f)} == {PART1_EXAMPLE_OUTPUT}?")

    with open(INPUT_FILE_PATH) as f:
        print(part_1(f))

    # with io.StringIO(EXAMPLE) as f:
    #     print(f"{part_2(f)} == {PART2_EXAMPLE_OUTPUT}?")

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_2(f))
