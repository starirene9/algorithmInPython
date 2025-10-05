class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    '''
    1. root와 맨 끝의 위치를 바꾼다.
    2. 바뀐 root_node 를 자식과 비교
    3. 자식들이 크다면, 둘 중 더 큰 자식과 위치 바꾸기 
    4. 이 과정을 바닥을 찍을때까지, 혹은 내가 자식보다는 클때까지 반복
    5. 그리고 나서 1번의 root 노드를 반환 
    '''

    def delete(self):
        # 구현해보세요!
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        prev_max = self.items.pop()

        cur_idx = 1

        while cur_idx <= len(self.items) - 1:
            left_child_idx = cur_idx * 2
            right_child_idx = cur_idx * 2 + 1
            max_idx = cur_idx

            if left_child_idx <= len(self.items) - 1 and self.items[left_child_idx] > self.items[max_idx]:
                max_idx = left_child_idx

            if right_child_idx <= len(self.items) - 1 and self.items[right_child_idx] > self.items[max_idx]:
                max_idx = right_child_idx

            if max_idx == cur_idx:
                break

            self.items[cur_idx], self.items[max_idx] = self.items[max_idx], self.items[cur_idx]
            cur_idx = max_idx

        return prev_max   # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]