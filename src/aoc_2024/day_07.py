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


def comb2_reduction(head, tail, total):
    """
    from itertools import permutations
    import pprint
    from pprint import pprint
        doesn't work due to
        7290: 6 8 6 15
        causing a floating point result for integer division
        even after fixing that it's tricky due to floating point .0
    """
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
        copy_total = total
        total_digits = []
        while copy_total // 10 != 0:
            total_digits = [copy_total % 10] + total_digits
            copy_total = copy_total // 10
        total_digits = [copy_total] + total_digits

        splits = []
        for i in range(1, len(total_digits)):
            split = [total_digits[:i], total_digits[i:]]
            splits.extend(split)

        return (
            comb2_reduction(head[:-1], head[-1], total - tail)
            or comb2_reduction(head[:-1], head[-1], total / tail)
            or any([comb2_reduction(head[:-1], head[-1], t) for t in splits])
        )


# def comb2(head, tail, total):
#     if len(head) == 1:
#         # tail = tail[0]
#         head = head[0]
#         # print(head, tail)
#         return (
#             head * tail, head + tail, int(str(head) + str(tail))
#         )
#     else:
#         for option in
#         return (
#             tail + comb2(head[:-1], head[-1]) == total
#             or comb2(head[:-1], head[-1]) == total
#             or any([comb2(head[:-1], head[-1], t) for t in splits] == total)
#         )


EXAMPLE = """7290: 6 8 6 15"""

EXAMPLE = """6815: 6 8 15"""


def comb2(head, tail, total, all_combos=[]):
    if len(head) == 1:
        # tail = tail[0]
        head = head[0]
        # print(head, tail)
        return (head * tail, head + tail, int(str(head) + str(tail)))
        return (
            (head, "*", tail),
            (head, "+", tail),
            (head, "||", tail),
        )
    else:
        new_head = head[:-1]
        new_tail = head[-1]
        combos = comb2(new_head, new_tail, total, all_combos)

        for combo in combos:
            all_combos.extend(
                [
                    (combo, "+", tail),
                    (combo, "*", tail),
                    (combo, "||", tail),
                ]
            )
            # all_combos.extend([
            #     (combo, '+', tail),
            #     (combo, '*', tail),
            #     (combo, '||', tail),
            # ])
            # pprint(all_combos)

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


def part_2(file):
    ans = 0
    for line in file:
        # print(total, line)
        total, els = line.strip().split(":")
        els = [int(e) for e in els.strip().split()]
        total = int(total)
        # print(total, els)
        combos = comb2(els[:-1], els[-1], total, [])
        # pprint(combos, width=150)
        for combo in combos:
            ans += total
            print(combo)
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
