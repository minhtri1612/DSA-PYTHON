# viết giải thuật để loại bỏ các giá trị giống nhau trong danh sách

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

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.data,end=" ")
            current_node = current_node.next
    def remove_trunglap(self):
        if self.head is None:
            return
        
        current = self.head
        seen = set([current.data])
        while current.next is not None:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next
            
ll = LinkedList()
ll.insertHead(10)
ll.insertHead(10)
ll.insertHead(43)
ll.insertHead(11)
ll.insertHead(23)
ll.insertHead(10)
ll.insertHead(90)
ll.insertHead(20)
ll.insertHead(40)
ll.insertHead(10)
ll.insertHead(12)
ll.insertHead(30)
ll.print_list()
ll.remove_trunglap()
print()
ll.print_list()

            