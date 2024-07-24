class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_the_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

ll = LinkedList()
ll.insert_at_the_beginning(10)
ll.insert_at_the_beginning(20)
ll.insert_at_the_beginning(30)

ll.print_list()
