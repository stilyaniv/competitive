def execute_code(operations):
    accumulator = 0
    stack_pointer = 0
    executed_lines_indices = []

    while stack_pointer not in executed_lines_indices:
        executed_lines_indices.append(stack_pointer)
        current_op, increment = operations[stack_pointer]
        if current_op == "nop":
            stack_pointer += 1
        elif current_op == "jmp":
            stack_pointer += increment
        elif current_op == "acc":
            stack_pointer += 1
            accumulator += increment

    return accumulator

def execute_and_fix_code(operations):
    accumulator = 0
    stack_pointer = 0
    execute_ops_indices = []
    verified_ops_indices = []
    currently_verifying = None

    while stack_pointer < len(operations):
        if stack_pointer in execute_ops_indices:
            verified_ops_indices.append(currently_verifying)
            accumulator = 0
            stack_pointer = 0
            execute_ops_indices = []
            currently_verifying = None

        current_op, increment = operations[stack_pointer]
        execute_ops_indices.append(stack_pointer)
        if current_op == "nop":
            if currently_verifying is None and stack_pointer not in verified_ops_indices:
                currently_verifying = stack_pointer
                stack_pointer += increment
            else:
                stack_pointer += 1
        elif current_op == "jmp":
            if currently_verifying is None and stack_pointer not in verified_ops_indices:
                currently_verifying = stack_pointer
                stack_pointer += 1
            else:
                stack_pointer += increment
        elif current_op == "acc":
            accumulator += increment
            stack_pointer += 1

    return accumulator


def load_operations_from_file(input_file_path):
    operations = []
    with open(input_file_path) as file:
        for line in file:
            operation, increment = line.split()
            operations.append((operation, int(increment)))
    return operations

def execute_code_file(input_file_path):
    ops = load_operations_from_file(input_file_path)
    return execute_code(ops)

def execute_and_fix_code_file(input_file_path):
    ops = load_operations_from_file(input_file_path)
    return execute_and_fix_code(ops)

if __name__ == "__main__":
    print(execute_code_file("day_8_input.txt"))
    print(execute_and_fix_code_file("day_8_input.txt"))
