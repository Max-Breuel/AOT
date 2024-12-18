import re


def second_star_filter(received_operation):
    global operation_is_valid # Global used to maintain a single return value to the function
    value_to_check = re.sub("[()0-9,]*", "", received_operation)

    match value_to_check:
        case "do":
            operation_is_valid = True
            return 0
        case "don't":
            operation_is_valid = False
            return 0
        case "mul":
            if operation_is_valid:
                return perform_multiplication(received_operation)
    return 0


def perform_multiplication(operation_str):
    filtered_str = re.sub(r"[A-Za-z()]*", "", operation_str)
    x, y = filtered_str.split(",")
    return int(x.strip()) * int(y.strip())


with open("puzzle_input.txt") as puzzle_input:
    total_sum_1 = 0
    total_sum_2 = 0
    operation_is_valid = True
    for line in puzzle_input:
        valid_operation = re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", line)

        for operation in valid_operation:
            if operation.startswith("mul"):
                total_sum_1 += perform_multiplication(operation)
            total_sum_2 += second_star_filter(operation)

print("first challenge answer:", total_sum_1)
print("second challenge answer:", total_sum_2)