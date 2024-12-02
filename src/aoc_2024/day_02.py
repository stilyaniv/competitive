"""
https://adventofcode.com/2024/day/2
"""
import timeit
import logging
import io

EXAMPLE = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


INPUT_FILE_PATH = r"src/aoc_2024/day_02.txt"


def validate_line(line):
    state = None
    broken_level_index = 0
    for i, report in enumerate(line):
        if i == 0:
            continue
        elif i >= 1:
            previous_report = line[i - 1]
            if report == previous_report:
                broken_level_index = i
                break
            elif report > previous_report:
                if state is None:
                    state = "inc"
                elif state is not None:
                    if state == "dec":
                        broken_level_index = i
                        break
                if 1 <= abs(report - previous_report) <= 3:
                    continue
                else:
                    broken_level_index = i
                    break
            elif report < previous_report:
                if state is None:
                    state = "dec"
                elif state is not None:
                    if state == "inc":
                        broken_level_index = i
                        break
                if 1 <= abs(report - previous_report) <= 3:
                    continue
                else:
                    broken_level_index = i
                    break
    return broken_level_index == 0, broken_level_index


def part_1(file):
    safe_reports = []
    unsafe_reports = []
    for line in file:
        line = list(map(int, line.split()))
        is_valid, broken_level_i = validate_line(line)
        if is_valid:
            safe_reports.append(line)
        else:
            unsafe_reports.append(line)
    print(safe_reports)
    print(unsafe_reports)
    return len(safe_reports)


def part_2(file):
    safe_reports = []
    unsafe_reports = []
    for line in file:
        line = list(map(int, line.split()))
        is_valid, _ = validate_line(line)
        if is_valid:
            safe_reports.append(line)
        else:
            fixed = False
            for test_i in range(len(line)):
                fixed_line = [level for i, level in enumerate(line) if i != test_i]
                if validate_line(fixed_line)[0]:
                    safe_reports.append(line)
                    fixed = True
                    break
            if not fixed:
                unsafe_reports.append(line)
    # print(safe_reports)
    # print(unsafe_reports)
    return len(safe_reports)


def part_2_performance():
    with open(INPUT_FILE_PATH) as f:
        t = timeit.Timer(lambda: part_2(f))
        timing = t.repeat(repeat=5, number=10 ** 6)
        print(timing)


if __name__ == "__main__":
    with io.StringIO(EXAMPLE) as f:
        print(part_1(f))

    with open(INPUT_FILE_PATH) as f:
        print(part_1(f))

    with io.StringIO(EXAMPLE) as f:
        print(part_2(f))

    with open(INPUT_FILE_PATH) as f:
        print(part_2(f))

    part_2_performance()
