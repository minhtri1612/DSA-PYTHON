class Stack:
    def __init__(self):
        self._data=[]
    
    def __len__(self):
        return len(self._data)
    
    def push(self,data):
        self._data.append(data)
        
    def pop(self):
        return self._data.pop()
    
    def peek(self):
        return self._data[len(self._data)-1]
stack=Stack()
stack.push(10)
stack.push(3)
stack.push(66)
stack.push(23)
stack.push(14)
test=stack.pop()
alo=stack.peek()
print(test)
print(alo)
for i in range(16):
    if i%3==0:
        stack.push(i)
    print(stack)
