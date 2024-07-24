class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data

    def free_stack(self):
        while self.top is not None:
            temp = self.top
            self.top = self.top.next
            del temp

if __name__ == "__main__":
    S = Stack()
    S.push(3)
    S.push(4)
    S.push(2)
    print(S.peek())  # Output: 2
    S.pop()
    print(S.peek())  # Output: 4
    
