class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.dummy_head=Node()
        
    def printList(self):
        current=self.dummy_head
        while current is not None:
            print(current.data)
            current=current.next
    
    def insertEnd(self,data):
        newNode=Node(data)
        current=self.dummy_head
        while current.next is not None:
            current=current.next
        current.next=newNode
        
    def insertPosition(self,data,n):
        newNode=Node(data)
        current=self.dummy_head
        i=1
        while (i<n):
            current=current.next
            i+=1
        newNode.next=current.next
        current.next=newNode
ll=LinkedList()
ll.insertEnd(4)
ll.insertEnd(3)
ll.insertEnd(2)
ll.insertEnd(1)
ll.insertEnd(0)
n=int(input("nhap tu ban phim so n:"))
ll.insertPosition(9,n)
ll.printList()