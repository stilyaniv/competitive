EXAMPLE = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""


def part_1():
    col1, col2 = [], []
    # for row in EXAMPLE.splitlines():
    for row in open(r"src/aoc_2024/day_01.txt"):
        left, right = row.split()
        col1.append(int(left))
        col2.append(int(right))
    total = sum(abs(left - right) for left, right in zip(sorted(col1), sorted(col2)))
    return total


def part_2():
    total = 0
    col1, col2 = [], []
    # for row in EXAMPLE.splitlines():
    for row in open(r"src/aoc_2024/day_01.txt"):
        left, right = row.split()
        col1.append(int(left))
        col2.append(int(right))
    for num in col1:
        times_found = 0
        for right in col2:
            if num == right:
                times_found += 1

        total += num * times_found
    return total


if __name__ == "__main__":
    print(part_2())
