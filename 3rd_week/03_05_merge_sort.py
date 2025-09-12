array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

def merge_sort(array):
    if len(array) <= 1:
        return array # 1보다 작다면 그냥 배열 반환

    mid = (0 + len(array)) // 2
    left_array = merge_sort(array[:mid])   # 왼쪽 부분을 정렬하고
    right_array = merge_sort(array[mid:])  # 오른쪽 부분을 정렬한 다음에

    return merge(left_array, right_array)         # 합치면서 정렬하면 됩니다!


def merge(array1, array2):

    result = []
    array1_index = 0
    array2_index = 0

    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else :
            result.append(array2[array2_index])
            array2_index += 1

    while array1_index < len(array1):
        result.append(array1[array1_index])
        array1_index += 1

    while array2_index < len(array2):
        result.append(array2[array2_index])
        array2_index += 1

    return result

print(merge(array_a, array_b))