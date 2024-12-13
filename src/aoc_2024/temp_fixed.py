def part_2(file):
    # ... (rest of your code)

    while first_empty < file_start:
        if new_line[file_end - 1] == ".":
            file_start -= 1
            file_end -= 1
        elif new_line[first_empty] != ".":
            first_empty += 1
        else:
            # Find the leftmost empty space
            empty_start = first_empty
            while empty_start < len(new_line) and new_line[empty_start] == ".":
                empty_start += 1
            empty_end = empty_start - 1

            # Check if the current file fits
            file_size = file_end - file_start
            space_size = empty_end - empty_start
            if space_size >= file_size:
                # Move the file to the leftmost free space
                new_line[empty_start:empty_start + file_size] = new_line[file_start:file_end]
                new_line[file_start:file_end] = ["."] * file_size
                first_empty = empty_start + file_size
            else:
                # Move to the next file
                file_end = file_start
                file_start -= 1

    # ... (rest of your code)

    return checksum_pos
