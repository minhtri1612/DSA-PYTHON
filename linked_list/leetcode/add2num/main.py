# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            sum_val = carry + x + y
            carry = sum_val // 10
            current.next = ListNode(sum_val % 10)
            current = current.next
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry > 0:
            current.next = ListNode(carry)
        
        return dummy_head.next

# Helper function to create a linked list from a list of numbers
def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for number in lst:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(node):
    while node is not None:
        print(node.val, end=' ')
        node = node.next
    print()

# Test the solution
l1 = create_linked_list([1, 4, 3])
l2 = create_linked_list([5, 6, 4])
solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print("Output:")
print_linked_list(result)
