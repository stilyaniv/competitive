"""
https://adventofcode.com/2024/day/1
"""
import io

EXAMPLE = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

INPUT_FILE_PATH = r"day_99.txt"


def part_1(file):
    dial = 50
    count = 0
    for row in file:
        row = row.strip()
        letter = row[0]
        num = int(row[1:])
        print(dial, letter, num, end=" -> ")
        num = num % 100
        if letter == "R":
            dial += num
            if dial > 99:
                dial -= 100
        elif letter == "L":
            dial -= num
            if dial < 0:
                dial += 100
        if dial == 0:
            count += 1
        print(dial)

    return count


def part_2(file):
    dial = 50
    count = 0
    for row in file:
        row = row.strip()
        letter = row[0]
        num = int(row[1:])
        print(dial, letter, num, end=" = ")
        rot = num % 100
        multiplier = num // 100
        prev_dial = dial
        if letter == "R":
            dial += rot
            if dial > 99:
                print(dial, end=" -> ")
                dial -= 100
                count += 1
        elif letter == "L":
            dial -= rot
            if dial < 0:
                print(dial, end=" -> ")
                dial += 100
                if prev_dial != 0:
                    count += 1
            if dial == 0:
                count += 1

        count += multiplier

        print(dial, f", passed zero {count} in total")

    return count


if __name__ == "__main__":
    # with io.StringIO(EXAMPLE) as f:
    #     print(part_1(f))  # 3

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_1(f))
    # 274 too low

    with io.StringIO(EXAMPLE) as f:
        print(part_2(f))  # 6

    with open(INPUT_FILE_PATH) as f:
        print(part_2(f))  # 6561

    # 3377 too low, 6580 too high
