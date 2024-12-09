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

INPUT_FILE_PATH = f"{Path(__file__).parent / Path(__file__).stem}.txt"

PART1_EXAMPLE_OUTPUT = 1928
PART2_EXAMPLE_OUTPUT = None


def part_1(file):
    padded_line = []
    line = file.readline().strip() + "0"
    file_id = 0
    for i in range(0, len(line), 2):
        padded_line.extend(int(line[i]) * [str(file_id)])
        padded_line.extend(int(line[i + 1]) * ["."])
        file_id += 1

    left, right = 0, len(padded_line) - 1
    new_line = list(padded_line)
    while left < right:
        if padded_line[left] == "." and padded_line[right] != ".":
            new_line[left], new_line[right] = new_line[right], new_line[left]
            left += 1
            right -= 1
        elif padded_line[left] != "." and padded_line[right] != ".":
            left += 1
        elif padded_line[left] != "." and padded_line[right] == ".":
            right -= 1
        elif padded_line[left] == "." and padded_line[right] == ".":
            right -= 1
        else:
            raise Exception

    print(line)
    print("".join(padded_line))
    print("".join(new_line))

    checksum_pos = 0
    block_index = 0
    checksum_b = 0
    for pos, item in enumerate(new_line):
        if item == ".":
            continue
            # item = "0"
        if item != "0":
            print(f"{pos} * {int(item)} = {pos * int(item)}")
        checksum_pos += pos * int(item)
        # print(f"{block_index} * {int(item)} = {block_index * int(item)}")
        checksum_b += block_index * int(item)
        block_index += 1
    return checksum_pos, checksum_b


# 0 * 0 = 0,
# 1 * 0 = 0,
# 2 * 9 = 18,
# 3 * 9 = 27,
# 4 * 8 = 32


def part_2(file):
    for line in file:
        pass

    return


if __name__ == "__main__":
    with io.StringIO(EXAMPLE) as f:
        print(f"{part_1(f)} == {PART1_EXAMPLE_OUTPUT}?")

    with open(INPUT_FILE_PATH) as f:
        print(part_1(f))
    # 89636261147   wrong   counting chars not whole files, checksum with block
    # 91190059546 too low   counting chars not whole files, checksum with i
    # 6617457194559 wrong
    # 7684649426862 too high
    # 6617705487250 too high

    # with io.StringIO(EXAMPLE) as f:
    #     print(f"{part_2(f)} == {PART2_EXAMPLE_OUTPUT}?")

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_2(f))
