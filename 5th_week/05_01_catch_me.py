from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    """
    queue사용 deque
    코니 각 초마다 C+1 <- 시간이라는 변수 설정과 어떻게 값이 변하는지 체크
    브라운 B-1, B+1, 2*B <- 경우의 수 여러개면 DFS, BFX & 시간과 함께 변화하는 값은 배열안에 해시 구조가 적합
    둘다 조건문 0 <= 위치p <=200000
    둘다 나가면 게임 종료
    """

    time = 0
    queue = deque()
    queue.append((brown_loc, 0))
    # 위치를 기준으로 시간이 몇 초 였는지 기록

    visited = [{} for _ in range(200001)] #[{}, {}, {} 이런게 20만개의 형태]
    # visited[10] = {시간 : True} 이런 식으로 값 저장할 예정

    while cony_loc <= 200000:
        cony_loc += time
        if time in visited[cony_loc]: # 브라운과 코니의 로케이션에 대한 시간이 정확히 일치한다는 것
            return time

        for i in range(0, len(queue)): # while queue를 쓰지 않고 for 문은 쓰는 이유는? 현재시간 기준으로만 queue를 뽑고 싶음
            current_position, current_time = queue.popleft()

            new_time = current_time + 1

            new_position = current_position - 1
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True # 위치 중심으로 새로운 시간의 키값일때 true 값을 설정
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = 2 * current_position
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

        time += 1
    return


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))