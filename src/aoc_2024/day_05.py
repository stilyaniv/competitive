"""
https://adventofcode.com/2024/day/5
"""
from functools import cmp_to_key
from pprint import pprint
import io
from pathlib import Path

EXAMPLE = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
INPUT_FILE_PATH = f"{Path(__file__).parent / Path(__file__).stem}.txt"


def part_1(file):
    lines = []
    children = {}
    parents = {}
    for line in file:
        line = line.strip()
        if line == "\n":
            continue
        elif "|" in line:
            parent, child = line.strip().split("|")
            if parent in children:
                children[parent].append(child)
            else:
                children[parent] = [child.strip()]
            if child in parents:
                parents[child].append(parent)
            else:
                parents[child] = [parent.strip()]
        elif "," in line:
            lines.append(line.split(","))
    pprint(children)
    pprint(parents)
    print(lines)

    valid_lines = []
    invalid_lines = []
    mid_total = 0
    for line in lines:
        valid_line = True
        for i, num in enumerate(line):
            print(f"checking {num} at index {i}")
            for l in range(0, i):
                print(l)
                if num in children and line[l] in children[num]:
                    valid_line = False
                    break
            for r in range(i + 1, len(line)):
                print(r)
                if num in parents and line[r] in parents[num]:
                    valid_line = False
                    break
        if valid_line:
            valid_lines.append(line)
            mid_total += int(line[len(line) // 2])
        else:
            invalid_lines.append(line)
    print(valid_lines)
    print(invalid_lines)

    return mid_total


def bigger_than(x, y, children):
    if x not in children:
        return False
    elif y not in children:
        return True

    if x in children[y]:
        return False

    return True


def part_2(file):
    # initialize item hierarchy and inputs to check
    lines = []
    children = {}
    parents = {}
    for line in file:
        line = line.strip()
        if line == "\n":
            continue
        elif "|" in line:
            parent, child = line.strip().split("|")
            if parent in children:
                children[parent].append(child)
            else:
                children[parent] = [child.strip()]
            if child in parents:
                parents[child].append(parent)
            else:
                parents[child] = [parent.strip()]
        elif "," in line:
            lines.append(line.split(","))

    # find invalid lines
    valid_lines = []
    invalid_lines = []
    mid_total = 0
    for line in lines:
        valid_line = True
        for i, num in enumerate(line):
            print(f"checking {num} at index {i}")
            for l in range(0, i):
                print(l)
                if num in children and line[l] in children[num]:
                    valid_line = False
                    break
            for r in range(i + 1, len(line)):
                print(r)
                if num in parents and line[r] in parents[num]:
                    valid_line = False
                    break
        if valid_line:
            valid_lines.append(line)
            mid_total += int(line[len(line) // 2])
        else:
            invalid_lines.append(line)

    def bigger_than(x, y):
        if x not in children:
            return False
        elif y not in children:
            return True

        if x in children[y]:
            return False

        return True

    corrected_lines = []
    for line in invalid_lines:
        corrected_lines.append(sorted(line, key=cmp_to_key(bigger_than)))

    mid_total = 0
    for line in corrected_lines:
        print(line)
        mid_total += int(line[len(line) // 2])

    return mid_total


if __name__ == "__main__":
    with io.StringIO(EXAMPLE) as f:
        print(part_1(f))

    with open(INPUT_FILE_PATH) as f:
        print(part_1(f))

    with io.StringIO(EXAMPLE) as f:
        print(part_2(f))

    with open(INPUT_FILE_PATH) as f:
        print(part_2(f))
