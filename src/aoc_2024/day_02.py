"""
https://adventofcode.com/2024/day/2
"""
import io

EXAMPLE = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

# # first example, skip either of the 4s and it's fine
# EXAMPLE = """\
# 8 6 4 4 1
# """

# second example, only skipping the 6 works
# EXAMPLE = """\
# 9 6 5 1
# """

# EXAMPLE = """\
# 1 2 7 8 9
# 9 7 6 2 1
# """

INPUT_FILE_PATH = r"src/aoc_2024/day_02.txt"


def part_1(file):
    safe_reports = []
    unsafe_reports = []
    for line in file:
        state = None
        line = list(map(int, line.split()))
        for i, report in enumerate(line):
            if i == 0:
                continue
            elif i >= 1:
                previous_report = line[i - 1]
                if report == previous_report:
                    unsafe_reports.append(line)
                    break
                elif report > previous_report:
                    if state is None:
                        state = "inc"
                    elif state is not None:
                        if state == "dec":
                            unsafe_reports.append(line)
                            break
                    if 1 <= abs(report - previous_report) <= 3:
                        continue
                    else:
                        unsafe_reports.append(line)
                        break
                elif report < previous_report:
                    if state is None:
                        state = "dec"
                    elif state is not None:
                        if state == "inc":
                            unsafe_reports.append(line)
                            break
                    if 1 <= abs(report - previous_report) <= 3:
                        continue
                    else:
                        unsafe_reports.append(line)
                        break
        if line not in unsafe_reports:
            safe_reports.append(line)
    print(safe_reports)
    print(unsafe_reports)
    return len(safe_reports)


def validate_line(line):
    state = None
    broken_levels = 0
    for i, report in enumerate(line):
        if broken_levels >= 1:
            return False, i - 1
        if i == 0:
            continue
        elif i >= 1:
            if broken_levels == 0:
                previous_report = line[i - 1]
            else:
                previous_report = line[i - 2]
            if report == previous_report:
                broken_levels += 1
                continue
            elif report > previous_report:
                if state is None:
                    state = "inc"
                elif state is not None:
                    if state == "dec":
                        broken_levels += 1
                        continue
                if 1 <= abs(report - previous_report) <= 3:
                    continue
                else:
                    broken_levels += 1
                    continue
            elif report < previous_report:
                if state is None:
                    state = "dec"
                elif state is not None:
                    if state == "inc":
                        broken_levels += 1
                        continue
                if 1 <= abs(report - previous_report) <= 3:
                    continue
                else:
                    broken_levels += 1
                    continue
    if broken_levels >= 1:
        return False, i
    else:
        return True, None


def part_2(file):
    safe_reports = []
    unsafe_reports = []
    for line in file:
        line = list(map(int, line.split()))
        is_valid, broken_level_index = validate_line(line)
        if is_valid:
            safe_reports.append(line)
        else:
            fixed = False
            for i, level in enumerate(line):
                broken_level_index = i
                fixed_line = [
                    level for i, level in enumerate(line) if i != broken_level_index
                ]
                if validate_line(fixed_line)[0]:
                    safe_reports.append(line)
                    fixed = True
                    break
            if not fixed:
                unsafe_reports.append(line)
    print(safe_reports)
    print(unsafe_reports)
    return len(safe_reports)


if __name__ == "__main__":
    with io.StringIO(EXAMPLE) as f:
        print(part_1(f))

    with open(INPUT_FILE_PATH) as f:
        print(part_1(f))

    # with io.StringIO(EXAMPLE) as f:
    #     print(part_2(f))

    # with open(INPUT_FILE_PATH) as f:
    #     print(part_2(f))
