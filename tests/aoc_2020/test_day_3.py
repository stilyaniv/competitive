from src.aoc_2020 import day_3

INPUT_GRID = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
""".split()


def test_count_trees_example():
    assert 7 == day_3.count_trees(INPUT_GRID, 3, 1)


def test_count_trees_challenge():
    with open(day_3.INPUT_FILE_PATH) as file:
        grid = file.read().split()
    assert 198 == day_3.count_trees(grid, 3, 1)


def test_count_trees_many_slopes():
    with open(day_3.INPUT_FILE_PATH) as file:
        grid = file.read().split()
    slopes = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )
    assert 5140884672 == day_3.count_trees_many_slopes(grid, slopes)