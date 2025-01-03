from pprint import pprint

"""
https://adventofcode.com/
"""  # TODO link to problem
import io
from pathlib import Path

EXAMPLE = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""  # TODO small size example from problem

INPUT_FILE_PATH = f"{Path(__file__).parent / Path(__file__).stem}.txt"


def part_1(file):

    grid = []
    for y, line in enumerate(file):
        row = []
        for x, char in enumerate(line.strip()):
            if char == "^":
                guard_pos = x, y
            row.append(char)
        grid.append(row)

    height = len(grid)
    width = len(grid[0])
    pprint(grid)
    print(guard_pos)
    directions = (0, -1), (1, 0), (0, 1), (-1, 0)
    dir_idx = 0
    x, y = guard_pos
    visited = [guard_pos]
    while 0 < y < height - 1 and 0 < x < width - 1:
        print(dir_idx % 4)
        print(x, y)
        direction = directions[dir_idx % 4]
        next = (x + direction[0], y + direction[1])
        next_box = grid[next[1]][next[0]]
        if next_box == "#":
            dir_idx += 1
            continue
        x, y = next
        visited.append((x, y))
    print(visited)
    print(len(set(visited)))
    return len(set(visited))


def part_2(file):
    grid = []
    for y, line in enumerate(file):
        row = []
        for x, char in enumerate(line.strip()):
            if char == "^":
                start_pos = x, y
            row.append(char)
        grid.append(row)

    height = len(grid)
    width = len(grid[0])

    x, y = start_pos

    # x1, y1 = (56, 28)
    # grid[y1][x1] = "O"
    # pprint(grid, width=400)
    visited, _, is_loop = traverse(grid, y, x, height, width, 0, start_pos)

    visited = sorted(visited)
    # TODO slow
    options = []
    for x1, y1, _ in visited:
        print(x1, y1)
        is_loop = False
        if grid[y1][x1] == "#":
            continue
        grid[y1][x1] = "O"
        visited, _, is_loop = traverse(
            grid, y, x, height, width, 0, start_pos, [], False
        )
        if is_loop:
            options.append((x1, y1))
        grid[y1][x1] = "."

    return len(set(options))


def traverse(grid, y, x, height, width, dir_idx, start_pos):
    directions = (0, -1), (1, 0), (0, 1), (-1, 0)
    (x, y) = start_pos
    visited = [(x, y, dir_idx)]
    options = []

    while 0 < y < height - 1 and 0 < x < width - 1:
        dir_idx = dir_idx % 4
        direction = directions[dir_idx]
        next_i = (x + direction[0], y + direction[1])
        next_box = grid[next_i[1]][next_i[0]]
        print(f"{dir_idx}: {(x,y)} -> {next_i} {next_box}")
        if next_box == "#" or next_box == "O":
            if (x, y, dir_idx) in visited[:-1]:
                return visited, options, True
            dir_idx += 1
            continue
        x, y = next_i
        visited.append((x, y, dir_idx))
    return visited, options, False


if __name__ == "__main__":
    with io.StringIO(EXAMPLE) as f:
        print(part_1(f))

    with open(INPUT_FILE_PATH) as f:
        print(part_1(f))

    with io.StringIO(EXAMPLE) as f:
        print(part_2(f))

    with open(INPUT_FILE_PATH) as f:
        print(part_2(f))
