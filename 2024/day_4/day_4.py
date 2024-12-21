def get_info_from_file(filename):
    matrix = []
    with open(filename) as file:
        for line in file:
            matrix.append(line.replace("\n", "").strip())

    return matrix


def get_horizontal_words(line_len, x_pos, line):
    local_count = 0
    if x_pos + 3 < line_len:
        if line[x_pos:x_pos + 4] == "XMAS":  # Slice the string to get the correct pattern
            local_count += 1
    if x_pos - 3 >= 0:
        if line[x_pos - 3:x_pos + 1] == "SAMX": # Slice the string to get the correct pattern
            local_count += 1
    return local_count


def get_vertical_words(x_height, x_pos, matrix):
    local_count = 0



#char_matrix = get_info_from_file("puzzle_input.txt")
#
#height = len(char_matrix)
#length = len(char_matrix[0])
#
#for i in range(height):
#    for j in range(length):
