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
    # lines = [[char for char in line.strip()] for line in file]
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
    return


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
    pprint(grid)

    x, y = start_pos
    visited, options, last_idx = traverse(
        grid, y, x, height, width, 0, start_pos, [], False
    )

    print(visited)
    print(len(set(visited)))
    print(options)
    print(len(set(options)))
    return len(set(options))


def traverse(grid, y, x, height, width, dir_idx, start_pos, options_tested, trial):
    directions = (0, -1), (1, 0), (0, 1), (-1, 0)
    # dir_idx = 0
    visited = [(x, y)]
    right_turns = 0
    options = []
    # options_tested = []
    while 0 < y < height - 1 and 0 < x < width - 1:
        dir_idx = dir_idx % 4
        direction = directions[dir_idx]
        next_i = (x + direction[0], y + direction[1])
        next_box = grid[next_i[1]][next_i[0]]
        print(f"{dir_idx}: {(x,y)} -> {next_i} {next_box} {right_turns}")
        # if (x, y) in visited[:-1] and right_turns == 3:
        #     options.append(next_i)
        #     if trial:
        #         return [], options
        #     right_turns = 0
        if next_box == "#":
            if trial and (x, y) in visited[-1]:
                return visited, options, (x, y)
            dir_idx += 1
            right_turns = right_turns + 1
            continue
        elif not trial and next_i not in options_tested:
            original = (x, y)
            original_dir_idx = dir_idx
            options_tested.append(next_i)
            grid[next_i[1]][next_i[0]] = "#"
            a, b, last_idx = traverse(
                grid, y, x, height, width, dir_idx, (x, y), options_tested, True
            )
            if last_idx == start_pos:
                options.append(next_i)
            grid[next_i[1]][next_i[0]] = "."
            x, y = original
            dir_idx = original_dir_idx
        x, y = next_i
        visited.append((x, y))
    return visited, options, (x, y)


if __name__ == "__main__":
    with io.StringIO(EXAMPLE) as f:
        print(part_1(f))  # 41

    with open(INPUT_FILE_PATH) as f:
        print(part_1(f))  # 5551

    # TODO infinite loop
    # with io.StringIO(EXAMPLE) as f:
    #     print(part_2(f))

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_2(f))
