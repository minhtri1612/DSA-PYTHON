class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertHead(self,data):
        new_Node=Node(data)
        new_Node.next = self.head
        self.head = new_Node

    def delete_head(self):
        temp= self.head
        self.head=self.head.next
        del (temp)

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.data,end=" ")
            current_node = current_node.next

ll = LinkedList()
ll.insertHead(10)
ll.insertHead(20)
ll.insertHead(30)
ll.print_list()
print("\n")
ll.delete_head()
ll.print_list()

        