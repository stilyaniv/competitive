def sum_top_n_stacks(n=1):
    top_stacks = []
    current_stack = 0
    for line in open(r"./src/aoc_2022/day1.txt"):
        if line == "\n":
            new_top_stacks = []
            is_new_inserted = False
            i = 0
            while not is_new_inserted:
                if i >= len(top_stacks):
                    new_top_stacks.append(current_stack)
                    is_new_inserted = True
                else:
                    top_stack_i = top_stacks[i]
                    if current_stack >= top_stack_i:
                        new_top_stacks.append(current_stack)
                        is_new_inserted = True
                    else:
                        new_top_stacks.append(top_stack_i)
                        i += 1
            current_stack = 0
            while i < len(top_stacks):
                new_top_stacks.append(top_stacks[i])
                i += 1
            top_stacks = new_top_stacks
        else:
            current_stack += int(line)
    print(top_stacks)
    return sum(top_stacks[:n])


def part_1():
    return sum_top_n_stacks(n=1)


def part_2():
    return sum_top_n_stacks(n=3)


if __name__ == "__main__":
    print(part_1())  # 72240
    print(part_2())  # 210957
