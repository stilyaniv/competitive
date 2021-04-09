INPUT_FILE_PATH = "inputs/day_6_input.txt"

def get_sum_of_any_yes_from_file(input_file_path):
    count = 0
    current_group = set()
    with open(input_file_path) as file:
        for line in file:
            if len(line.strip()) == 0:
                count += len(current_group)
                current_group = set()
                continue
            current_group.update(list(line.strip()))
        current_group.update(list(line.strip()))
        count += len(current_group)
    return count


def get_sum_of_all_yes_from_file(input_file_path):
    result_count = 0
    current_group = {}
    members_count = 0
    num_all_corrects = 0
    with open(input_file_path) as file:
        for line in file:
            if len(line.strip()) == 0:
                for count in current_group.values():
                    num_all_corrects += members_count == count
                result_count += num_all_corrects
                current_group = {}
                members_count = 0
                num_all_corrects = 0
                continue
            for answer in line.strip():
                try:
                    current_group[answer] += 1
                except KeyError:
                    current_group[answer] = 1
            members_count += 1
        members_count += 1
        for answer in line.strip():#TODO DRY
            try:
                current_group[answer] += 1
            except KeyError:
                current_group[answer] = 1
        for count in current_group.values():
            num_all_corrects += members_count == count
        result_count += num_all_corrects
    return result_count


if __name__ == "__main__":
    print(get_sum_of_any_yes_from_file(INPUT_FILE_PATH))
    print(get_sum_of_all_yes_from_file(INPUT_FILE_PATH))
    