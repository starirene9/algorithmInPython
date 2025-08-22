def find_max_plus_or_multiply(array):
    # max_value = 0
    # if len(array) >= 2:
    #     plus_value = array[0] + array[1]
    #     multiply_value = array[0] * array[1]
    #     max_value = max(plus_value, multiply_value)
    # for number in array[2:]:
    #     plus_value = max_value + number
    #     multiply_value = max_value * number
    #     max_value = max(plus_value, multiply_value)
    # return max_value

    # 강의 풀이법
    """
    값이 0이면 더하는게 곱하는거 보다 낫고
    모든 합이 1이면 곱하는거 보다 더하는게 낫다 라는 사실에 착안한다.
    """
    plus_or_multiply_sum = 0
    for num in array:
        if num <=1 or plus_or_multiply_sum <=1:
            plus_or_multiply_sum += num
        else:
            plus_or_multiply_sum *= num
    return plus_or_multiply_sum

"""
len(array) 
첫 두개 array[0] + array[1]  를 더하거나 곱하고 큰 값을 맥스로 저장하고 
그 다음 인덱스 array[2] 를 더하거나 곱해보고 큰 값을 다음 맥스로 더하고 
그 다다음 array[3] 인덱스 
"""

result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))