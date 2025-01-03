"""
https://adventofcode.com/2024/day/4
"""
import time
import pprint
import io
from pathlib import Path

EXAMPLE = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

INPUT_FILE_PATH = f"{Path(__file__).parent / Path(__file__).stem}.txt"


# TODO combine into iterating once over the whole grid
def part_1(file):
    lines = [[char for char in line.strip()] for line in file]
    # print(lines)
    # print("\n".join(["".join(line) for line in lines]))
    # pprint.pprint(lines)
    total_count = 0
    for l, line in enumerate(lines):
        for c, char in enumerate(line):
            try:
                next_4 = line[c : c + 4]
            except IndexError:
                continue
            # print(next_4)
            if "".join(next_4) == "XMAS" or "".join(next_4) == "SAMX":
                total_count += 1
    print(total_count)
    for c in range(len(lines)):
        for r in range(len(lines)):
            try:
                next_4 = (
                    lines[r][c] + lines[r + 1][c] + lines[r + 2][c] + lines[r + 3][c]
                )
            except IndexError:
                continue
            # print(next_4)
            if "".join(next_4) == "XMAS" or "".join(next_4) == "SAMX":
                total_count += 1
    print(total_count)
    for r in range(len(lines)):
        for c in range(len(lines)):
            try:
                n1, n2, n3, n4 = (
                    lines[r][c],
                    lines[r + 1][c + 1],
                    lines[r + 2][c + 2],
                    lines[r + 3][c + 3],
                )
                next_4 = n1, n2, n3, n4
                # box = ([(["·" for c in range(len(lines))]) for r in range(len(lines))])
                # box[r][c] = n1
                # box[r+1][c+1] = n2
                # box[r+2][c+2] = n3
                # box[r+3][c+3] = n4
                # box = "\n".join([" ".join(c for c in line) for line in box])
                # print(box)
                # print()
            except IndexError:
                continue
            # print(next_4)
            if "".join(next_4) == "XMAS" or "".join(next_4) == "SAMX":
                # print('yes')
                total_count += 1
    print(total_count)
    for r in range(0, len(lines) - 3):
        for c in range(3, len(lines)):
            try:
                # co1, co2, co3, co4 = (r, c), (r+1, c-1), (r+2, c-2), (r+3, c-3),
                n1, n2, n3, n4 = (
                    lines[r][c],
                    lines[r + 1][c - 1],
                    lines[r + 2][c - 2],
                    lines[r + 3][c - 3],
                )
                next_4 = n1, n2, n3, n4
                # box = ([(["·" for c in range(len(lines))]) for r in range(len(lines))])
                # box[r][c] = n1
                # box[r+1][c-1] = n2
                # box[r+2][c-2] = n3
                # box[r+3][c-3] = n4
                # box = "\n".join([" ".join(c for c in line) for line in box])
                # print(box)
                # print()
            except IndexError:
                continue
            # print(next_4)
            if "".join(next_4) == "XMAS" or "".join(next_4) == "SAMX":
                # print('yes')
                total_count += 1
    return total_count


PART_2_CHOICES = (
    """\
M · S
· A ·
M · S
""",
    """\
M · M
· A ·
S · S
""",
    """\
S · M
· A ·
S · M
""",
    """\
S · S
· A ·
M · M
""",
)


def part_2(file, visualise=False):
    grid = [[char for char in line.strip()] for line in file]
    total_count = 0
    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid) - 1):
            ti = r - 1
            bi = r + 1
            li = c - 1
            ri = c + 1
            tl = grid[ti][li]
            bl = grid[bi][li]
            tr = grid[ti][ri]
            br = grid[bi][ri]
            md = grid[r][c]
            found = f"{tl} · {tr}\n" f"· {md   } ·\n" f"{bl} · {br}\n"
            if visualise:
                print(found)

            if found in PART_2_CHOICES:
                total_count += 1
    return total_count


if __name__ == "__main__":
    with io.StringIO(EXAMPLE) as f:
        print(part_1(f))

    with open(INPUT_FILE_PATH) as f:
        print(part_1(f))

    with io.StringIO(EXAMPLE) as f:
        print(part_2(f, visualise=True))

    with open(INPUT_FILE_PATH) as f:
        print(part_2(f))
