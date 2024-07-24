class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def findMiddle(self,head):
        fast=slow=head
        while head.next and fast.next.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow
    def mergeSort(self,left,right):
        result=None
        
        