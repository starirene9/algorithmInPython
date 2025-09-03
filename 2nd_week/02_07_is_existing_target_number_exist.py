# finding_target = 14
# finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
#
#
# def is_existing_target_number_sequential(target, array):
#     for number in array:
#         if target == number:
#             return True
#
#     return False
#
#
# result = is_existing_target_number_sequential(finding_target, finding_numbers)
# print(result)  # True

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    min_num_index = 0
    max_num_index = len(array) - 1
    current_guess = (min_num_index + max_num_index) // 2

    find_count = 0
    while min_num_index <= max_num_index:
        find_count += 1
        if array[current_guess] == target:
            print(find_count)
            return True
        elif array[current_guess] < target:
            min_num_index = current_guess + 1
        else:
            max_num_index = current_guess - 1
        current_guess = (min_num_index + max_num_index) // 2 #줄어든 범위에서 다음 탐색값을 찾는 행위
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)