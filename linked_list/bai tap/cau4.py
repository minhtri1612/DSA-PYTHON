#hoán đổi 2 nút liền kề trong LInked list
# input: 1 -> 3 -> 4 -> 7 -> 9 -> 21 -> 43
# output:3 -> 1 -> 7 -> 4 -> 21 -> 9 -> 43
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insertEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def hoandoi(self):
        if self.head is None or self.head.next is None:
            return

        # Initialize pointers
        prev = None
        current = self.head
        self.head = current.next  # Change head to the second node

        while current is not None and current.next is not None:
            next_node = current.next
            next_next = next_node.next

            # Swap current and next_node
            next_node.next = current
            current.next = next_next

            
            
    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.data,end=" ")
            current_node = current_node.next

ll = LinkedList()
ll.insertEnd(1)
ll.insertEnd(3)
ll.insertEnd(4)
ll.insertEnd(7)
ll.insertEnd(9)
ll.insertEnd(21)
ll.insertEnd(43)
ll.print_list()
print("after hoan doi:")
ll.hoandoi()
ll.print_list()
