"""
https://adventofcode.com/
"""  # TODO link to problem
import io
from pathlib import Path
from pprint import pprint

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


INPUT_FILE_PATH = f"{Path(__file__).parent / Path(__file__).stem}.txt"


def comb1(head, tail, total):
    if len(head) == 1:
        head = head[0]
        return (
            head * tail == total
            or head + tail == total
            or int(str(head) + str(tail))
            == total  # TODO restore comb1 to the part 1 solution
        )
    else:
        splits = []
        for i in range(1, len(str(total))):
            split = [int(str(total)[:i]), int(str(total)[i:])]
            splits.extend(split)

        return (
            comb1(head[:-1], head[-1], total - tail)
            or comb1(head[:-1], head[-1], total / tail)
            or any(
                [comb1(head[:-1], head[-1], t) for t in splits]
            )  # TODO restore comb1 to the part 1 solution
        )


def part_1(file):
    ans = 0
    for line in file:
        # print(total, line)
        total, els = line.strip().split(":")
        els = [int(e) for e in els.strip().split()]
        total = int(total)
        print(total, els)
        if comb1(els[:-1], els[-1], total):
            ans += total
    return ans


"""
    part 2
    ------
    190: 10 19 has only one position that accepts an operator: between 10 and 19. Choosing + would give 29, but choosing * would give the test value (10 * 19 = 190).
    3267: 81 40 27 has two positions for operators. Of the four possible configurations of the operators, two cause the right side to match the test value: 
            81 + 40 * 27 and 81 * 40 + 27 both equal 3267 (when evaluated left-to-right)!
    156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
    192: 17 8 14 can be made true using 17 || 8 + 14.
    292: 11 6 16 20 can be solved in exactly one way: 11 + 6 * 16 + 20.

    7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
"""

# EXAMPLE = """\
# 190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20
# """

# EXAMPLE = """6815: 6 8 15"""
# EXAMPLE = """161011: 16 10 13"""

# 7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
#  48 || 6 * 15
#    486   * 15
# EXAMPLE = """7290: 6 8 6 15"""

"""
head    tail    total
[6 8 6] 15      7290
.[6 8 6] * 15    7290               !!!
..[6 8] 6         486 = 7290 // 15  
...[6 8] * 6       486              !!!
....6 8             81 = 486 // 6
....6 + 8           14
....6 * 8           48
....6 || 8          68
...[6 8] + 6       486
....6 8             480 = 486 - 6
....6 + 8           14
....6 * 8           48
....6 || 8          68
...[6 8] || 6      486              !!!
....6 8             48 = 48 << 6     
....6 + 8           14
....6 * 8           48              !!!
....6 || 8          68
.[6 8 6] + 15      7290
.[6 8 6] || 15      7290

"""


def comb2_reduction(head, tail, total):
    """
    from itertools import permutations
    import pprint
    from pprint import pprint
        doesn't work due to:
        7290: 6 8 6 15
        causing a floating point result for integer division
        even after fixing that it's tricky due to floating point .0
    """
    print(head, tail, total)
    if len(head) == 1:
        # print(head, tail)
        head = head[0]
        return (
            head * tail == total
            or head + tail == total
            or int(str(head) + str(tail)) == total
        )
    else:
        # copy_total = total
        # total_digits = []
        # while copy_total // 10 != 0:
        #     total_digits = [copy_total % 10] + total_digits
        #     copy_total = copy_total // 10
        # total_digits = [copy_total] + total_digits

        # total_digits = str(total)
        # splits = []
        # for i in range(1, len(total_digits)):
        #     split = [total_digits[:i], total_digits[i:]]
        #     splits.extend(split)

        # print(head[:-1], head[-1], total)
        # start_next = len(str(tail))

        total = int(total)
        return (
            comb2_reduction(head[:-1], head[-1], total - tail)
            or (
                total % tail == 0
                and comb2_reduction(head[:-1], head[-1], total // tail)
            )
            or (
                str(total) != str(tail)
                and str(total).endswith(str(tail))
                and comb2_reduction(
                    head[:-1], head[-1], int(str(total)[: -len(str(tail))])
                )
            )
        )


def part_2(file):
    ans = 0
    for line in file:
        total, els = line.strip().split(":")
        els = [int(e) for e in els.strip().split()]
        total = int(total)
        valid = comb2_reduction(els[:-1], els[-1], total)
        if valid:
            ans += total
            print(f"{total} == {els}")
    return ans


if __name__ == "__main__":
    # with io.StringIO(EXAMPLE) as f:
    #     print(part_1(f))

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_1(f))

    # with io.StringIO(EXAMPLE) as f:
    #     print(part_2(f))  # 11387

    with open(INPUT_FILE_PATH) as f:
        print(part_2(f))
