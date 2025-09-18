class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return  print("Queue is empty")
        delete_head = self.head
        self .head = self.head.next
        return delete_head

    def peek(self):
        if self.is_empty():
            return print("Queue is empty")
        return self.head.data

    def is_empty(self):
        return self.head is None

# Queue는 항상 맨 앞의 것이 출력되서 나옴
queue = Queue()
queue.enqueue(1)
print(queue.peek())
queue.enqueue(2)
print(queue.peek())
queue.enqueue(3)

queue.dequeue()
print(queue.peek())

queue.dequeue()
print(queue.peek())
