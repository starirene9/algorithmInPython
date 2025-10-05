class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 구현해보세요!
        self.items.append(value)
        cur_idx = len(self.items) - 1

        while cur_idx != 1:
            # 부모 노드랑 비교해서 내가 더 크다면 위치 바꿈
            parent_idx = cur_idx // 2
            if self.items[cur_idx] > self.items[parent_idx]:
                self.items[cur_idx], self.items[parent_idx] = self.items[parent_idx], self.items[cur_idx]
                cur_idx = parent_idx
            else:
                break
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!