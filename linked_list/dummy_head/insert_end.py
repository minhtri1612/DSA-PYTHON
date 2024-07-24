class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.dummy_head=Node()
        
    def insertEnd(self,data):
        newNode=Node(data)
        current=self.dummy_head
        while current.next is not None:
            current=current.next
        current.next=newNode
        
    def printList(self):
        current=self.dummy_head.next
        while current is not None:
            print(current.data,end=" -> ") 
            current=current.next
            
ll=LinkedList()
ll.insertEnd(4)
ll.insertEnd(3)
ll.insertEnd(2)
ll.insertEnd(1)
ll.insertEnd(0)
ll.printList()
