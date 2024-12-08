"""
https://adventofcode.com/2024/day/7
"""

import io
from pathlib import Path

EXAMPLE = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

PART1_EXAMPLE_OUTPUT = 3749
PART2_EXAMPLE_OUTPUT = 11387
PART1_OUTPUT = 303876485655
PART2_OUTPUT = 146111650210682

INPUT_FILE_PATH = f"{Path(__file__).parent / Path(__file__).stem}.txt"


def comb1(head, tail, total):
    if len(head) == 1:
        head = head[0]
        return head * tail == total or head + tail == total
    else:
        return comb1(head[:-1], head[-1], total - tail) or comb1(
            head[:-1], head[-1], total / tail
        )


def part_1(file):
    ans = 0
    for line in file:
        total, els = line.strip().split(":")
        els = [int(e) for e in els.strip().split()]
        total = int(total)
        if comb1(els[:-1], els[-1], total):
            ans += total
    return ans


def comb2(head, tail, total):
    print(f"{head} _ {tail} == {total}?")
    if len(head) == 1:
        head = head[0]

        return (
            head * tail == total
            or head + tail == total
            or int(str(head) + str(tail)) == total
        )
    else:
        return (
            comb2(head[:-1], head[-1], total - tail)
            or (total % tail == 0 and comb2(head[:-1], head[-1], total // tail))
            or (
                str(total) != str(tail)
                and str(total).endswith(str(tail))
                and comb2(head[:-1], head[-1], int(str(total)[: -len(str(tail))]))
            )
        )


def part_2(file):
    ans = 0
    for line in file:
        total, els = line.strip().split(":")
        els = [int(e) for e in els.strip().split()]
        total = int(total)
        valid = comb2(els[:-1], els[-1], total)
        if valid:
            ans += total
    return ans


if __name__ == "__main__":
    with io.StringIO(EXAMPLE) as f:
        print(f"{part_1(f)} == {PART1_EXAMPLE_OUTPUT}?")

    with open(INPUT_FILE_PATH) as f:
        print(f"{part_1(f)} == {PART1_EXAMPLE_OUTPUT}?")

    with io.StringIO(EXAMPLE) as f:
        print(f"{part_2(f)} == {PART1_OUTPUT}?")

    with open(INPUT_FILE_PATH) as f:
        print(f"{part_2(f)} == {PART2_OUTPUT}?")
