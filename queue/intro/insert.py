class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None
    
    def insertBegin(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode 
            
    def printLIst(self):
        current=self.head
        while current is not None:
            print(current.data,end=" ")
            current=current.next
        print("\n")
    def deleteNode(self):
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
ll=LinkList()
ll.insertBegin(3)
ll.insertBegin(4)
ll.insertBegin(1)
ll.insertBegin(2)
ll.printLIst()
ll.deleteNode()
ll.printLIst()
