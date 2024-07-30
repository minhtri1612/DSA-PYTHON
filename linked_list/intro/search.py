class Node:
    def __init__(self,data):
        self.next=None
        self.data=data

class LinkeList:
    def __init__(self):
        self.head = None
        
    def create_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()
        
    def search(self,target):
        current = self.head
        while current is not None and current.data != target:
            current=current.next
        return current is not None
    
    def insertBegin(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        
ll=LinkeList()
ll.insertBegin(3)
ll.insertBegin(4)
ll.insertBegin(2)
ll.insertBegin(1)
print("Search for 3:", ll.search(3))
ll.create_list()
