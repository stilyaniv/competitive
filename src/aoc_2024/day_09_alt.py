"""
https://adventofcode.com/
"""  # TODO link to problem

import io
from pathlib import Path

EXAMPLE = """\
2333133121414131402
"""
# EXAMPLE = """\
# 12345
# """

INPUT_FILE_PATH = f"{Path(__file__).parent}day_09.txt"

PART1_EXAMPLE_OUTPUT = 1928
PART2_EXAMPLE_OUTPUT = 2858


class File:

    def __init__(self, pos_idx, file_id, size):
        self.pos_idx = pos_idx
        self.file_id = file_id
        self.size = size
        self.moved = False


def part_2(file):
    disk_str = file.readline().strip() + "0"

    disk = []
    file_id = 0
    for file_id in range(0, len(disk_str), 2):
        f = File(int(file_id), file_id, int(file_id))
        disk.append(f)
        disk.append(int(disk_str[file_id + 1]))
        file_id += 1
    return disk


if __name__ == "__main__":
    with io.StringIO(EXAMPLE) as f:
        print(f"{part_2(f)} == {PART2_EXAMPLE_OUTPUT}?")

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_2(f))

    # 6273568034328 wrong
    # 6287327755269 too high
    # 6287341702001 too high
    # 6287343722737
    # 6287404501347 too high
    # 6287527318218
