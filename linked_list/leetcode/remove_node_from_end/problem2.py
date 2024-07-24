class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy_head = ListNode(0)
        dummy_head.next = head
        first = second = dummy_head
        
        for i in range(n + 1):
            if first is not None:
                first = first.next
        
        while first is not None:
            first = first.next
            second = second.next
        
        temp = second.next
        second.next = temp.next
        del temp
        
        return dummy_head.next

def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for number in lst:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

def print_linked_list(node):
    while node is not None:
        print(node.val, end=' -> ')
        node = node.next
    print("None")

head = create_linked_list([1, 2, 3, 4, 5])
n = 2
solution = Solution()
print_linked_list(head)
result = solution.removeNthFromEnd(head, n)
print_linked_list(result)
