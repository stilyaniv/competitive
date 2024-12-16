"""
https://adventofcode.com/
"""  # TODO link to problem
import io
import re
from pathlib import Path
from pprint import pprint
from typing import List

PART_1_EXAMPLE = """\
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""


INPUT_FILE_PATH = f"{Path(__file__).parent / Path(__file__).stem}.txt"

PART_1_EXAMPLE_OUTPUT = 480
PART_2_EXAMPLE_OUTPUT = None

X_Y_PATTERN = r"X.(\d*), Y.(\d*)"


def create_grid(file):
    grid = []
    special_chars = {}
    x_len, y_len = 0, 0
    for y, line in enumerate(file):
        y_len += 1
        row = []
        for x, char in enumerate(line.strip()):
            row.append(char)
            if char in special_chars:
                special_chars[char] += [(x, y)]
            else:
                special_chars[char] = [(x, y)]
        grid.append(row)

    x_len, y_len = x + 1, y + 1
    return grid, x_len, y_len, special_chars


# PART_1_EXAMPLE = """\
# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400
# """


def part_1(file):
    lines = f.readlines()
    machines = []
    for i in range(0, len(lines), 4):
        xa, ya = re.search(X_Y_PATTERN, lines[i].strip()).groups()
        xb, yb = re.search(X_Y_PATTERN, lines[i+1].strip()).groups()
        xp, yp = re.search(X_Y_PATTERN, lines[i+2].strip()).groups()
        machines.append([(int(xa), int(ya)), (int(xb), int(yb)), (int(xp), int(yp))])

    coins = 0
    for machine in machines:
        print(machine)
        (xa, ya), (xb, yb), (xp, yp) = machine
        winners = []
        for a in range(1, 101):
            for b in range(1, 101):
                # a = 80
                # b = 40
                if a*xa + b*xb == xp and a*ya + b*yb == yp:
                    price = 3*a + b
                    print(a, b, price)
                    winners.append(price)
        if winners:
            coins += min(winners)
        else:
            print(f"Machine has no winners {machine}")

    return coins


# PART_2_PART_1_EXAMPLE = """\
# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=10000000012748, Y=10000000012176
# """

# PART_2_PART_1_EXAMPLE = """\
# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=10000000012748, Y=10000000012176
# """

PART_2_EXAMPLE = """\
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=10000000008400, Y=10000000005400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=10000000012748, Y=10000000012176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=10000000007870, Y=10000000006450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=10000000018641, Y=10000000010279
"""

PART_2_INPUT_CHANGE = 10_000_000_000_000


def part_2(file):
    lines = f.readlines()
    machines = []
    for i in range(0, len(lines), 4):
        xa, ya = re.search(X_Y_PATTERN, lines[i].strip()).groups()
        xb, yb = re.search(X_Y_PATTERN, lines[i+1].strip()).groups()
        xp, yp = re.search(X_Y_PATTERN, lines[i+2].strip()).groups()
        machines.append([(int(xa), int(ya)),
                        (int(xb), int(yb)),
                        (int(xp)+PART_2_INPUT_CHANGE, int(yp)+PART_2_INPUT_CHANGE)])

    coins = 0
    for machine in machines:
        print(machine, end=' => ')
        (xa, ya), (xb, yb), (xp, yp) = machine

        # calculate matrix determinant
        # a*xa + b*xb = xp    D = | xa xb    Da = | xp xb    Db = | xa xp
        # a*ya + b*yb = yp        | ya yb         | yp yb         | ya yp

        D = xa*yb - ya*xb
        Da = xp*yb - yp*xb
        Db = xa*yp - ya*xp

        if Da % D == 0 and Db % D == 0:
            a = Da // D
            b = Db // D
            price = 3*a + b
            coins += price
            print(a, b, price)
        else:
            print(f"{machine} has no winners.")

    return coins


if __name__ == "__main__":
    # with io.StringIO(PART_1_EXAMPLE) as f:
    #     print(f"{part_1(f)} == {PART_1_EXAMPLE_OUTPUT}?")

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_1(f))

    # with io.StringIO(PART_2_EXAMPLE) as f:
    #     print(f"{part_2(f)} == {PART_2_EXAMPLE_OUTPUT}?")

    with open(INPUT_FILE_PATH) as f:
        print(part_2(f))
