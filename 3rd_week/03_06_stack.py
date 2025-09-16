class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
한 곳에서만 자료를 넣고 뺄 수 있다.
LIFO -> Last in First out 
가장 마지막에 넣은게 제일 빨리 나온다. 
'''

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        # push 맨 위의 값을 넣어줘
        new_head = Node(value) # [3]이란 노드를 만듦
        new_head.next = self.head # [3] -> [4]
        self.head = new_head # [3]이라는 노드를 head로 만듦

    # pop , 맨 위의 값을 빼줘
    def pop(self):
        if self.is_empty():
            return print("Stack is empty")
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):
        if self.is_empty():
            return print("Stack is empty")
        # 어떻게 하면 될까요?
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None

stack = Stack()
stack.push(1)
print(stack.head.data)

stack.push(2)
print(stack.head.data)

stack.push(3)
print(stack.peek())

stack.pop()
print(stack.peek())

stack.pop()
print(stack.peek())

stack.pop()
print(stack.peek())