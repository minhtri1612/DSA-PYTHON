#merge 2 Linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    # Create a dummy node to form the new linked list
    dummy = ListNode()
    current = dummy

    # Traverse both lists and add the smallest value node to the new list
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # If one of the lists is not empty, attach the remainder
    if l1:
        current.next = l1
    if l2:
        current.next = l2

    # Return the next node of the dummy since dummy is a placeholder
    return dummy.next

# Helper function to print the linked list
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Example usage
# Create first linked list: 1 -> 2 -> 4
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

# Create second linked list: 1 -> 3 -> 4
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

# Merge the lists
merged_list = merge_two_lists(l1, l2)

# Print the merged list
print_list(merged_list)
