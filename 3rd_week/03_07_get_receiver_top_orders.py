top_heights = [6, 9, 5, 7, 4]

# stop = -1 : range의 끝값은 포함되지 않으므로, 0까지 포함해 순회하려면 -1을 넣어야 합니다. 즉, j는 0까지 내려가지만 -1은 되지 않습니다.
def get_receiver_top_orders(heights):
    answer = [0] * len(heights)

    for i in range(len(heights) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if heights[i] <= heights[j]:
                answer[i] = j + 1
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))