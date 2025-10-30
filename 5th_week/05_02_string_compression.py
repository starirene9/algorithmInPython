input = "abcabcabcabcdededededede"

"""
문자열의 길이를 n이라고 한다면, 
1부터 n개까지 길이로 쪼갤 수 있다는 걸 의미. 
1 ~ n//2 (그 이상으로 넘어가면 반복이 안되서 의미 없음)

n = len(input)
print("n is", n)
for split_size in range(1, n, split_size) : 
    print(i, input[i:1 + split_size]) 
    # 1개의 길이로 자른 것 
"""
def string_compression(string):
    n = len(string)
    result = n
    for split_size in range(1, n // 2 + 1):
        splited = [
            string[i:i + split_size] for i in range(0, n, split_size)
        ]
        # print(splited)
        compressed = ""
        count = 1
        for i in range(0, len(splited) - 1):
            cur, next = splited[i], splited[i + 1]

            if cur == next:
                count += 1
            else:
                if count  == 1:
                    compressed += cur
                else:
                    compressed += f"{count}{cur}"
                count = 1
        if count == 1:
            compressed += splited[-1]
        else:
            compressed += f"{count}{splited[-1]}"
        # print("splited is", splited)
        # print("compressed is", compressed)
        result = min(len(compressed), result)
    return result


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))