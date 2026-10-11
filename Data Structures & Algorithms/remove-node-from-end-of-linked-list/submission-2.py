# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node,l = head,0
        while node :
            l+=1
            node = node.next
        node = dummy = ListNode()
        dummy.next = head
        for _ in range(l-n):
            node = node.next
        node.next = node.next.next
        return dummy.next
        