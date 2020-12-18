INPUT_FILE_PATH = "inputs/day_5_input.txt"

def get_row_id(string):
    return int(string.replace("F", "0").replace("B", "1"), 2)


def get_col_id(string):
    return int(string.replace("L", "0").replace("R", "1"), 2)


def get_seat_info(string):
    row_id = get_row_id(string[:7])
    col_id = get_col_id(string[7:])

    return row_id, col_id, row_id * 8 + col_id


def get_max_id_from_file():
    max_id = 0
    with open(INPUT_FILE_PATH) as file:
        for line in file:
            _, _, seat_id = get_seat_info(line.strip())
            if seat_id > max_id:
                max_id = seat_id
    return max_id


def insert_sorted(new, items):
    for idx, _ in enumerate(items):
        if new <= items[idx]:
            items.insert(idx, new)
            return
    items.append(new)


def get_missing_id_from_file():
    with open(INPUT_FILE_PATH) as file:
        ids = []
        for line in file:
            _, _, seat_id = get_seat_info(line.strip())
            insert_sorted(seat_id, ids)
    for idx in range(1,len(ids)-1):
        if ids[idx+1] - ids[idx] > 1:
            return ids[idx] + 1
        if ids[idx] - ids[idx-1] > 1:
            return ids[idx] - 1


if __name__ == "__main__":
    print(get_max_id_from_file())
    print(get_missing_id_from_file())
