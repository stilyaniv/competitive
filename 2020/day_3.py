def count_trees(grid, horizontalChange, verticalChange):
    colCount = len(grid[0])
    count = 0
    rowIdx = 0
    colIdx = 0
    while rowIdx < len(grid):
        colIdx = colIdx % colCount
        cell = grid[rowIdx][colIdx]
        colIdx += horizontalChange
        rowIdx += verticalChange
        count += cell == "#"

    return count


def count_trees_many_slopes(grid, slopes):
    multiple = 1
    for slope in slopes:
        multiple *= count_trees(grid, slope[0], slope[1])
    return multiple


if __name__ == "__main__":
    with open("day_3_input.txt") as file:
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
