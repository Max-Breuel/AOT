
def check_report_safety_part_1(report_list):
    is_increasing = True if report_list[0] < report_list[1] else False

    for i in range(len(report_list)-1):
        curr_step = abs(report_list[i] - report_list[i+1])
        if 0 <= curr_step <= 3:
            if is_increasing and report_list[i] > report_list[i+1]:
                return False
            if not is_increasing and report_list[i] < report_list[i+1]:
                return False
            if report_list[i] == report_list[i+1]:
                return False
        else:
            return False
    return True


def check_report_safety_part_2(report_list):

    if check_report_safety_part_1(report_list):
        return True

    for i in range(len(report_list)):
        edited_report = report_list[:i] + report_list[i+1:]
        if check_report_safety_part_1(edited_report):
            return True

    return False


with open("puzzle_input") as puzzle_input:
    safe_count_part_1 = 0
    safe_count_part_2 = 0
    for line in puzzle_input:
        reports_list = line.strip().split(" ")
        reports_list = list(map(int, reports_list))
        safe_count_part_1 += int(check_report_safety_part_1(reports_list))
        safe_count_part_2 += int(check_report_safety_part_2(reports_list))

print("First star code:", safe_count_part_1)
print("Second star code:", safe_count_part_2)
