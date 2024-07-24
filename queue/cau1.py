from collections import deque
class Queue:
    def __init__(self):
        self.queue=deque()
        
    def insert(self,item):
        self.queue.append(item)
        
    def delete(self):      
        return self.queue.popleft()
        
        
    def __str__(self):
        return str(self.queue)
    
my_queue=Queue()
my_queue.insert(100)
my_queue.insert(2)
my_queue.insert(34)
my_queue.insert(6)
print(my_queue)
print(my_queue.delete())
print(my_queue)

        
    