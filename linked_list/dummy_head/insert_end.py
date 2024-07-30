class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self._dummy = ListNode(value=-1)
        self._size = 0
        self._tail = None

    @property
    def size(self):
        return self._size
        
    def insertEnd(self, data):
        newNode = ListNode(data)
        current = self._dummy
        while current.next_node is not None:
            current = current.next_node
        current.next_node = newNode
        self._size += 1
    
    def remove_from_beginning(self):
        if self._dummy.next_node is None:
            return None
        remove_node = self._dummy.next_node
        self._dummy.next_node = self._dummy.next_node.next_node
        self._size -= 1
        return remove_node.value
    
    def printList(self):
        current = self._dummy.next_node
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next_node
        print("None")

# Test the LinkedList class
ll = LinkedList()
ll.insertEnd(4)
ll.insertEnd(3)
ll.insertEnd(2)
ll.insertEnd(1)
ll.insertEnd(0)

print("Original list:")
ll.printList()

ll.remove_from_beginning()

print("After removing from beginning:")
ll.printList()
