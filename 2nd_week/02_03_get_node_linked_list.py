
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

# LinkedList의 가장 끝에 있는 노드에 새로운 노드를 연결
    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_list(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0

        while cur_index != index:
            cur = cur.next
            cur_index += 1
        return cur


linked_list = LinkedList(5)
# print(linkedList.head.data)
linked_list.append(12)
linked_list.append(8)
print(linked_list.print_list())
print(linked_list.get_node(2).data)
