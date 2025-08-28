input = "011110"

"""
0에서 1을 만났을때 뒤집는다 : 모두 0으로 바꾸겠다
1에서 0을 만났을때 뒤집는다 : 모두 1로 바꾸겠다. 
"""

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_one = 0
    count_to_all_zero = 0

    if string[0] == "0":
        count_to_all_one += 1
    elif string[0] == "1":
        count_to_all_zero += 1

    for i in range(len(string) -1):
        if string[i] != string[i+1]:
            if string[i+1] == "1":
                count_to_all_zero += 1
            if string[i+1] == "0":
                count_to_all_one += 1
    return min(count_to_all_zero, count_to_all_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)