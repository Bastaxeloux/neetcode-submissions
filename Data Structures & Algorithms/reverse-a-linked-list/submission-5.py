# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None :
            return None
        a,b = None, head
        while b.next :
            c = b.next
            b.next = a
            a,b = b,c
        b.next = a
        return b

            