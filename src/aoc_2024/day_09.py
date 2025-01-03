"""
https://adventofcode.com/2024/day/9
"""

import io
from pathlib import Path

EXAMPLE = """\
2333133121414131402
"""

INPUT_FILE_PATH = f"{Path(__file__).parent / Path(__file__).stem}.txt"

PART1_EXAMPLE_OUTPUT = 1928
PART2_EXAMPLE_OUTPUT = 2858

DEBUG = False


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
    for pos, item in enumerate(new_line):
        if item == ".":
            continue
        checksum_pos += pos * int(item)
    return checksum_pos


# no spaces, shouldn't move anything
# EXAMPLE = """\
# 1010101010101010101
# """

# move last only, with 2 digit number
# EXAMPLE = """\
# 111010101010101010101
# """

# move when space is exactly adjacent to the file
# EXAMPLE = """\
# 122
# """

# skip one on the right and only move the next one
# EXAMPLE = """\
# 12203
# """


def print_pointers(original_list, left_pointers, right_pointers=[]):
    if not DEBUG:
        return
    new_list = []
    for i in range(len(original_list)):
        if i in left_pointers:
            new_list.append("l")
        elif i in right_pointers:
            new_list.append("r")
        else:
            new_list.append(" ")
    print("".join(original_list))
    print("".join(new_list))


def part_2(file):
    expanded_line = []
    line = file.readline().strip()
    if len(line) % 2 != 0:
        line = line + "0"
    smallest_file_id = 0
    for i in range(0, len(line), 2):
        expanded_line.extend(int(line[i]) * [str(smallest_file_id)])
        expanded_line.extend(int(line[i + 1]) * ["."])
        smallest_file_id += 1

    empty_start, empty_end = 0, 1
    file_start = len(expanded_line) - 2
    file_end = len(expanded_line) - 1
    new_line = list(expanded_line)
    print_pointers(new_line, [empty_start, empty_end], [file_start, file_end])
    while file_start >= 0:
        if expanded_line[file_end] == "." or int(expanded_line[file_end]) > smallest_file_id:
            file_end -= 1
            file_start -= 1
            print_pointers(new_line, [empty_start, empty_end], [file_start, file_end])
        elif expanded_line[file_end] != ".":
            while expanded_line[file_start] == expanded_line[file_end]:
                file_start -= 1
                print_pointers(new_line, [empty_start, empty_end], [file_start, file_end])
            file_size = file_end - file_start
            file_start += 1
            smallest_file_id = int(expanded_line[file_end])

            while True:
                # searching for a space
                while new_line[empty_start] != "." and empty_start < file_start:
                    empty_start += 1
                    empty_end += 1
                    print_pointers(new_line, [empty_start, empty_end], [file_start, file_end])
                while empty_end < file_start and new_line[empty_end] == ".":
                    empty_end += 1
                    print_pointers(new_line, [empty_start, empty_end], [file_start, file_end])

                # no more space to the left of current file
                if empty_end > file_start or empty_start >= file_start:
                    file_end = file_start - 1
                    file_start = file_end - 1
                    empty_start, empty_end = 0, 1
                    break
                else:
                    space_size = empty_end - empty_start
                    if space_size >= file_size:
                        while file_size > 0:
                            new_line[empty_start], new_line[file_end] = (
                                new_line[file_end],
                                new_line[empty_start],
                            )
                            file_size -= 1
                            empty_start += 1
                            file_end -= 1
                            print_pointers(new_line, [empty_start, empty_end], [file_start, file_end])
                        file_end = file_start - 1
                        file_start = file_end - 1
                        empty_start, empty_end = 0, 1
                        break
                    else:
                        empty_start = empty_end
                        empty_end = empty_start + 1
                    print_pointers(new_line, [empty_start, empty_end], [file_start, file_end])

    checksum_pos = 0
    for pos, item in enumerate(new_line):
        if item == ".":
            continue
        checksum_pos += pos * int(item)
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
