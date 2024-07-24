class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    
    def push(self,data):
        newNode=Node(data)
        newNode.next=self.top
        self.top=newNode
        
    def isEmpty(self):
        return self.top is None

        
    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        popped = self.top.data
        self.top = self.top.next
        return popped
    
    def peek(self):
        return self.top.data
    
stack=Stack()
stack.push(3)
stack.push(4)
stack.push(1)
stack.push(2)
stack.push(5)
print(stack.peek())