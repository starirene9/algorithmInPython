def find_max_num(array):
    max_num = array[0]
    for a in array:
        if a > max_num:
            max_num = a
    return max_num

    # for num in array:
    #     is_big_num = True #flag
    #     for num2 in array:
    #         if num < num2:
    #             is_big_num = False
    #     if is_big_num:
    #         return num



print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))