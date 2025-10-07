# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
visited = []


def dfs_recursion(adjacent_graph, cur_node, visited_array):
    # 구현해보세요!
    visited_array.append(cur_node)
    print('cur_node', cur_node, 'adjacent_graph[cur_node]', adjacent_graph[cur_node])
    print('visited_array', visited_array)
    for adjacent_node in adjacent_graph[cur_node]:
        if adjacent_node not in visited:
            dfs_recursion(adjacent_graph, adjacent_node, visited_array)
    return


dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!

'''
1. 시작 노드인 1부터 탐색
2. 현재 방문한 노드를 visited_array에 추가 
3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 방문 
'''