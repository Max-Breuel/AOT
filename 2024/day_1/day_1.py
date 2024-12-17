left_list = []
right_list = []
dist_list = []
total_dist_sum = 0

with open("puzzle_input.txt") as puzzle_input:
    for line in puzzle_input:
        left_list_data, right_list_data = line.split(" " * 3)  # split using file delimiter
        left_list.append(int(left_list_data))
        right_list.append(int(right_list_data.replace("\n", "")))

    left_list.sort()
    right_list.sort()

    for i in range(len(left_list)):
        curr_dist = abs(left_list[i] - right_list[i])
        dist_list.append(curr_dist)
        total_dist_sum += curr_dist

# first puzzle answer
print("first star answer:", total_dist_sum)

second_star_total_sum = 0
already_counted_num_dict = dict()

for i in range(len(left_list)):
    curr_num = left_list[i]
    if curr_num not in already_counted_num_dict.keys():
        already_counted_num_dict[curr_num] = 0

        for j in range(len(right_list)):
            if curr_num == right_list[j]:
                already_counted_num_dict[curr_num] += 1

        second_star_total_sum += curr_num * already_counted_num_dict[curr_num]

    else:
        second_star_total_sum += curr_num * already_counted_num_dict[curr_num]

# second puzzle answer
print("second star answer:", second_star_total_sum)
