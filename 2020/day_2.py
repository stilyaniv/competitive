def split_range(line):
    range, ruleChar, pwd = line.split()
    return range.split("-"), ruleChar[0], pwd


def is_valid_pass_in_range(entry):
    range, ruleChar, pwd = split_range(entry)
    count = 0
    for char in pwd:
        if char == ruleChar:
            count += 1
    return int(range[0]) <= count <= int(range[1])


def is_valid_pass_xor(entry):
    range, ruleChar, pwd = split_range(entry)
    idx1 = int(range[0]) - 1
    idx2 = int(range[1]) - 1
    return (pwd[idx1] == ruleChar) ^ (pwd[idx2] == ruleChar)


def count_valid_passwords(validatorFunc):
    with open("day_2_input.txt") as file:
        count = 0
        for line in file:
            count += validatorFunc(line)
        return count


def count_valid_passwords_range():
    return count_valid_passwords(is_valid_pass_in_range)


def count_valid_passwords_xor():
    return count_valid_passwords(is_valid_pass_xor)


if __name__ == "__main__":
    print(count_valid_passwords_range())
    print(count_valid_passwords_xor())