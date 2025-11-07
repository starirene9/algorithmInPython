from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

# 규칙성이 없고 다 실행해 봐야 알게 됨 -> 모든 수를 선택해도 괜찮은 범위 -> BFS
# Queue -> visited [0,1,3,4] 2배열 기준으로 방문했는지 여부를 확인
# 각 구슬이 어디어디 위치했는지가 궁금함. => 각 구슬이 방문했던 곳들을 중첩
#                               n       m        n         m
# visited 배열을 4차원으로 구성 [red_row][red_col][blue_row][blue_col]
# 3 <= n <= 10 의 사이 이므로 문제 없음

# 방향성 구현 : 항상 북동남서(상우하좌) 순서로 굴림
# 즉, BFS 한 단계(큐에서 하나 꺼냈을 때) →
# “위, 오른쪽, 아래, 왼쪽” 방향 순서로 각각 시뮬레이션을 해보며 가능한 다음 상태를 모두 큐에 넣습니다.
#     북  동  남  서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 벽이 닿던지 혹은 구멍에 닿던지
# diff_r, diff_c : 현재 이동해야하는 row, 현재 이동해야 하는 column
# 다음 이동이 벽이거나, 혹은 현재 위치가 구멍이라면 더이상 움직이지 않아야함

def move_until_wall_or_hole(r, c, diff_r, diff_c, game_map):
    move_count = 0

    while game_map[r + diff_r][c + diff_c] != "#" and game_map[r][c] != "O":
        r += diff_r
        c += diff_c
        move_count += 1

    return r, c, move_count


def is_available_to_take_out_only_red_marble(game_map):
    # 구현해보세요!
    n, m = len(game_map), len(game_map[0]) #행과 열
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)] #4차원 배열]
    queue = deque()
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_row, red_col = i, j
            if game_map[i][j] == "B":
                blue_row, blue_col = i, j
    queue.append((red_row, red_col, blue_row, blue_col, 1)) #이동했을때 어디에 위치해 있는가의 정보를 넣어야 함 + 몇 회 굴렸는지의 정보
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()
        print('red_row, red_col, blue_row, blue_col, try_count is', red_row, red_col, blue_row, blue_col, try_count)
        if try_count > 10: # 10회 이내여야 함
            break

        for i in range(4): # 구슬을 상하좌우로 이동시켜야 함
            next_red_row, next_red_col, red_move_count = move_until_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)
            next_blue_row, next_blue_col, blue_move_count = move_until_wall_or_hole(blue_row, blue_col, dr[i], dc[i], game_map)

            if game_map[next_blue_row][next_blue_col] == "O":
                continue # 얘를 제외하고 다음 후보자부터 탐색하겠다.

            if game_map[next_red_row][next_red_col] == "O":
                return True

            if next_red_row == next_blue_row and next_red_col == next_blue_col: # 한 칸에 구슬 하나만 -> move count가 많은 것을 이동
                if red_move_count > blue_move_count:
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]

            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count + 1))

    # print('visited is', visited)
    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다



game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
["#", "#", "#", "#", "#", "#", "#"],
["#", ".", ".", "R", "#", "B", "#"],
["#", ".", "#", "#", "#", "#", "#"],
["#", ".", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", ".", "#"],
["#", "O", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))