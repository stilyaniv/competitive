INPUT_FILE_PATH = "src/aoc_2020/inputs/day_2_input.txt"

def split_range(line):
    rule_range, rule_char, pwd = line.split()
    return rule_range.split("-"), rule_char[0], pwd


def is_valid_pass_in_range(entry):
    rule_range, rule_char, pwd = split_range(entry)
    count = 0
    for char in pwd:
        if char == rule_char:
            count += 1
    return int(rule_range[0]) <= count <= int(rule_range[1])


def is_valid_pass_xor(entry):
    rule_range, rule_char, pwd = split_range(entry)
    idx1 = int(rule_range[0]) - 1
    idx2 = int(rule_range[1]) - 1
    return (pwd[idx1] == rule_char) ^ (pwd[idx2] == rule_char)


def count_valid_passwords(validator_func):
    with open(INPUT_FILE_PATH) as file:
        count = 0
        for line in file:
            count += validator_func(line)
        return count


def count_valid_passwords_range():
    return count_valid_passwords(is_valid_pass_in_range)


def count_valid_passwords_xor():
    return count_valid_passwords(is_valid_pass_xor)


if __name__ == "__main__":
    print(count_valid_passwords_range())
    print(count_valid_passwords_xor())
