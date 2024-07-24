class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def insert_at_the_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete_end(self):
        if self.head is None:
            print("List is empty, nothing to delete")
            return
        if self.head.next is None:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next is not None:
            second_last = second_last.next
        second_last.next = None

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_the_end(3)
    ll.insert_at_the_end(4)
    ll.insert_at_the_end(1)
    ll.insert_at_the_end(2)
    ll.insert_at_the_end(5)
    ll.insert_at_the_end(7)
    ll.insert_at_the_end(8)

    print("List before deleting the end:")
    ll.create_list()

    ll.delete_end()

    print("List after deleting the end:")
    ll.create_list()
