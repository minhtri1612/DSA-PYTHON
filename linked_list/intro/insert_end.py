class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head =None

    def insert_End(self,data):
        new_Node=Node(data)
        if self.head is None:
            self.head = new_Node
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_Node
        
    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

ll = LinkedList()
ll.insert_End(10)
ll.insert_End(20)
ll.insert_End(30)

ll.print_list()