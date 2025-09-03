finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]
# 무작위 배열에서는 이진탐색을 찾을 수 없음 -> 정렬을 진행해야 함

def is_exist_target_number_binary(target, array):
    cur_min_num = 0
    cur_max_num = len(array) - 1
    cur_guess_num = cur_min_num + cur_max_num // 2

    while cur_guess_num <= target:
        if array[cur_guess_num] == target:
            return True
        elif array[cur_guess_num] < target:
            cur_min_num = cur_min_num + 1
        else:
            cur_max_num = cur_max_num - 1
        cur_guess_num = cur_guess_num + cur_guess_num // 2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)