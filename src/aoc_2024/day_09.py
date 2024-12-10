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
PART2_EXAMPLE_OUTPUT = 2858


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
        elif padded_line[left] != ".":
            left += 1
        elif padded_line[right] == ".":
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
    return checksum_pos


def part_2(file):
    padded_line = []
    line = file.readline().strip() + "0"
    file_id = 0
    for i in range(0, len(line), 2):
        padded_line.extend(int(line[i]) * [str(file_id)])
        padded_line.extend(int(line[i + 1]) * ["."])
        file_id += 1

    left, right = sub_left, sub_right = 0, len(padded_line) - 1
    new_line = list(padded_line)
    while left < right:
        # print(left, sub_left, sub_right, right)
        if padded_line[right] == ".":
            right -= 1
        elif padded_line[right] != ".":
            # current_file_id = padded_line[right]
            # left_file_id = padded_line[right - 1]
            sub_right = right - 1
            file = []
            while padded_line[sub_right] == padded_line[right]:
                sub_right -= 1
                # file.append(padded_line[right])
            file_size = right - sub_right

            found = False
            original_left = left
            while not found and left < sub_right:
                # print(left, sub_right)
                while new_line[left] != ".":
                    left += 1
                    # print(left, sub_left, sub_right, right)
                sub_left = left
                while new_line[sub_left] == ".":
                    sub_left += 1
                    # print(left, sub_left, sub_right, right)

                # TODO have to repeat below until we have no more spaces
                space_size = sub_left - left
                # print(f"{space_size >= file_size=}")
                if space_size >= file_size:
                    while file_size > 0:
                        new_line[left], new_line[right] = (
                            new_line[right],
                            new_line[left],
                        )
                        print("".join(new_line))
                        file_size -= 1
                        left += 1
                        right -= 1
                        # print(left, sub_left, sub_right, right)
                    found = True
                    # break
                else:
                    left = sub_left
                    # print(left, sub_left, sub_right, right)
                    # found = False``
            left = original_left
            right = sub_right
            # print(left, sub_left, sub_right, right)

            # while sub_left < sub_right + 1:
            #     if padded_line[sub_left] != ".":
            #         sub_left += 1
            #     else:

    # print(line)
    # print("".join(padded_line))
    # print("".join(new_line))

    checksum_pos = 0
    block_index = 0
    checksum_b = 0
    for pos, item in enumerate(new_line):
        if item == ".":
            continue
        # print(f"{pos} * {int(item)} = {pos * int(item)}")
        checksum_pos += pos * int(item)
        # print(f"{block_index} * {int(item)} = {block_index * int(item)}")
        checksum_b += block_index * int(item)
        block_index += 1
    return checksum_pos


if __name__ == "__main__":
    # with io.StringIO(EXAMPLE) as f:
    #     print(f"{part_1(f)} == {PART1_EXAMPLE_OUTPUT}?")

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_1(f))

    with io.StringIO(EXAMPLE) as f:
        print(f"{part_2(f)} == {PART2_EXAMPLE_OUTPUT}?")

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_2(f))

    # 6287404501347 too high
