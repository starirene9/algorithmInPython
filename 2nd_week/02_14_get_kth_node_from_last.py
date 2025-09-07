class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # length = 1
        # cur = self.head
        # while cur.next is not None:
        #     cur = cur.next
        #     length += 1
        # print("length of kth node is", length)
        # end_length = length - k
        # cur = self.head
        #
        # for i in range(end_length):
        #     cur = cur.next
        # return cur

        # 두 개의 포인터를 놓고 설정하는 방법
        slow_node = self.head
        fast_node = self.head

        for i in range(k):
            fast_node = fast_node.next

        while fast_node is not None:
            slow_node = slow_node.next
            fast_node = fast_node.next
        return slow_node


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(3).data)  # 7이 나와야 합니다!

"""
K개 거리만큼 떨어져있는 fast ,slow node를 구한다. 
"""