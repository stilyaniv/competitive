def top_n_stacks(num_needed=1):
    top_stacks = []
    current_stack = 0
    for line in open(r"./src/aoc_2022/day1.txt"):
        if line == "\n":
            new_top_stacks = []
            is_new_inserted = False
            i = 0
            while i < len(top_stacks):
                top_stack_i = top_stacks[i]
                if not is_new_inserted and current_stack >= top_stack_i:
                    new_top_stacks.append(current_stack)
                    is_new_inserted = True
                else:
                    new_top_stacks.append(top_stack_i)
                    i += 1
            if not is_new_inserted:
                new_top_stacks.append(current_stack)
            top_stacks = new_top_stacks
            current_stack = 0
        else:
            current_stack += int(line)

    return top_stacks[:num_needed]


def part_1():
    return sum(top_n_stacks(1))


def part_2():
    return sum(top_n_stacks(3))


if __name__ == "__main__":
    print(part_1())  # 72240
    print(part_2())  # 210957
