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
"""  # TODO small size example from problem


INPUT_FILE_PATH = f"{Path(__file__).parent / Path(__file__).stem}.txt"


def comb1(head, tail, total):
    if len(head) == 1:
        # tail = tail[0]
        head = head[0]
        # print(head, tail)
        return (
            head * tail == total
            or head + tail == total
            or int(str(head) + str(tail)) == total
        )
    else:
        splits = []
        for i in range(1, len(str(total))):
            split = [int(str(total)[:i]), int(str(total)[i:])]
            splits.extend(split)

        return (
            comb1(head[:-1], head[-1], total - tail)
            or comb1(head[:-1], head[-1], total / tail)
            or any([comb1(head[:-1], head[-1], t) for t in splits])
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


def comb2(head, tail, total, all_combos=[]):
    if len(head) == 1:
        head = head[0]
        # tail = tail[0]
        # print(head, tail)
        return (
            (head, "*", tail),
            (head, "+", tail),
            (head, "||", tail),
        )
        # return (head * tail, head + tail, int(str(head) + str(tail)))
    else:
        new_head = head[:-1]
        new_tail = head[-1]
        combos = comb2(new_head, new_tail, total, all_combos)

        for combo in combos:
            # all_combos.extend(
            #     [
            #         (combo + tail),
            #         (combo * tail),
            #         (int(str(combo) + str(tail))),
            #     ]
            # )
            all_combos.extend(
                [
                    (combo, "+", tail),
                    (combo, "*", tail),
                    (combo, "||", tail),
                ]
            )
            pprint(all_combos)

        # for combo in comb2(new_head, new_tail, total, combs):
        #     # combo = comb2(new_head, new_tail, total, combs)
        #     combos.append((
        #         (("*", tail),  combo),
        #         (("+", tail),  combo),
        #         (("||", tail),  combo),
        #     ))
        return all_combos

        # return (
        #     tail + comb2(new_head, new_tail, total) == total
        #     or tail * comb2(new_head, new_tail, total) == total
        #     or int(str(tail) + str(comb2(new_head, new_tail, total)) == total
        # )


def comb3(head, tail, total, op):
    if len(head) == 1:
        head = head[0]
        # tail = tail[0]
        # print(head, tail)
        if op == "+":
            return head + tail
        elif op == "*":
            return head * tail
        elif op == "||":
            return int(str(head) + str(tail))
    else:
        new_head = head[:-1]
        new_tail = head[-1]
        combos1 = comb3(new_head, new_tail, total, "*")
        combos2 = comb3(new_head, new_tail, total, "+")
        combos3 = comb3(new_head, new_tail, total, "||")

        return


def comb2(head, tail, total):
    if len(head) == 1:
        # tail = tail[0]
        head = head[0]
        # print(head, tail)
        return (head * tail, head + tail, int(str(head) + str(tail)))
    else:
        # for option in
        return (
            tail + comb2(head[:-1], head[-1]) == total
            or comb2(head[:-1], head[-1]) == total
            or any([comb2(head[:-1], head[-1], t) for t in splits] == total)
        )


"""
    190: 10 19 has only one position that accepts an operator: between 10 and 19. Choosing + would give 29, but choosing * would give the test value (10 * 19 = 190).
    3267: 81 40 27 has two positions for operators. Of the four possible configurations of the operators, two cause the right side to match the test value: 
            81 + 40 * 27 and 81 * 40 + 27 both equal 3267 (when evaluated left-to-right)!
    156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
    192: 17 8 14 can be made true using 17 || 8 + 14.
    292: 11 6 16 20 can be solved in exactly one way: 11 + 6 * 16 + 20.

    7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
"""

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


# 7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
#  48 || 6 * 15
#    486   * 15
EXAMPLE = """7290: 6 8 6 15"""


# EXAMPLE = """6815: 6 8 15"""
# EXAMPLE = """161011: 16 10 13"""


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
        # tail = tail[0]
        head = head[0]
        # print(head, tail)
        # print(
        #     head * tail, head + tail, int(str(head) + str(tail))
        # )
        splits = []
        total_str = str(total)
        for i in range(1, len(str(total))):
            split = [total_str[:i], total_str[i:]]
            splits.extend(split)
        return (
            head * tail == total
            or head + tail == total
            or any(int(str(head) + str(tail)) == total for total in splits)
        )
    else:
        # copy_total = total
        # total_digits = []
        # while copy_total // 10 != 0:
        #     total_digits = [copy_total % 10] + total_digits
        #     copy_total = copy_total // 10
        # total_digits = [copy_total] + total_digits

        # splits = []
        # for i in range(1, len(total_digits)):
        #     split = [total_digits[:i], total_digits[i:]]
        #     splits.extend(split)

        # print(head[:-1], head[-1], total)
        return (
            comb2_reduction(head[:-1], head[-1], total - tail)
            or (
                total % tail == 0
                and comb2_reduction(head[:-1], head[-1], total // tail)
            )  # 1) 15  3) 6 * 8
            # or any([comb2_reduction(head[:-1], head[-1], t) for t in splits])
            or comb2_reduction(
                head[:-1], head[-1], total
            )  # TODO critical when print(head,  tail, total) 2)
        )


def part_2(file):
    ans = 0
    for line in file:
        # print(total, line)
        total, els = line.strip().split(":")
        els = [int(e) for e in els.strip().split()]
        total = int(total)
        # print(total, els)
        valid = comb2_reduction(els[:-1], els[-1], total)
        # combos1 = comb3(els[:-1], els[-1], total, '+')
        # combos2 = comb3(els[:-1], els[-1], total, '*')
        # combos3 = comb3(els[:-1], els[-1], total, '||')
        # pprint(combos, width=150)
        # for combo in combos:
        if valid:
            ans += total
            print(f"{total} == {els}")
    return ans


# def part_2(file):
#     ans = 0
#     for line in file:
#         # print(total, line)
#         total, els = line.strip().split(":")
#         els = [int(e) for e in els.strip().split()]
#         total = int(total)
#         print(total, els)

#         from itertools import product
#         for item in product([1, 2, 3, 4], [1, 2]):
#             print(item)
#     return ans


if __name__ == "__main__":
    # with io.StringIO(EXAMPLE) as f:
    #     print(part_1(f))

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_1(f))

    with io.StringIO(EXAMPLE) as f:
        print(part_2(f))

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_2(f))
