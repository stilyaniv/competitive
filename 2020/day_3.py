INPUT_FILE_PATH = "inputs/day_3_input.txt"

def count_trees(grid, horizontal_change, vertical_change):
    col_count = len(grid[0])
    count = 0
    row_idx = 0
    col_idx = 0
    while row_idx < len(grid):
        col_idx = col_idx % col_count
        cell = grid[row_idx][col_idx]
        col_idx += horizontal_change
        row_idx += vertical_change
        count += cell == "#"

    return count


def count_trees_many_slopes(grid, slopes):
    multiple = 1
    for slope in slopes:
        multiple *= count_trees(grid, slope[0], slope[1])
    return multiple


if __name__ == "__main__":
    with open(INPUT_FILE_PATH) as file:
        grid = file.read().split()
    print(count_trees(grid, 3, 1))
    slopes = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )
    print(count_trees_many_slopes(grid, slopes))
