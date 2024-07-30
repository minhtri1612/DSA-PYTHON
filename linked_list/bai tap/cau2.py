# đảo ngược thứ tự danh sách có trong Linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertHead(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        
    def printList(self):
        current=self.head
        while current is not None:
            print(current.data,end=" ")
            current=current.next
        print()
        
    def reverse(self):
        prev_node = None
        current_node = self.head
        next_node = None
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node        
    
ll = LinkedList()
ll.insertHead(1)
ll.insertHead(2)
ll.insertHead(3)
ll.insertHead(4)
ll.insertHead(5)

print("Original linked list:")
ll.printList()

# Reverse the linked list
ll.reverse()

print("Reversed linked list:")
ll.printList()