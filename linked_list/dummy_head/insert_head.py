class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.dummy_head=Node()
        
    def insert_at_the_beginning(self,data):
        newNode=Node(data)
        newNode.next=self.dummy_head.next
        self.dummy_head.next=newNode
        
    def printList(self):
        current=self.dummy_head.next
        while current is not None:
            print(current.data)
            current=current.next
ll = LinkedList()
ll.insert_at_the_beginning(10)
ll.insert_at_the_beginning(20)
ll.insert_at_the_beginning(30)
ll.printList()
