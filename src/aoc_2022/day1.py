def part_1():
    max_stack, current_stack = 0, 0
    for line in open(r"./src/aoc_2022/day1.txt"):
        if line == "\n":
            if current_stack > max_stack:
                max_stack = current_stack
            current_stack = 0
        else:
            current_stack += int(line)
    return max_stack


if __name__ == "__main__":
    print(part_1())
