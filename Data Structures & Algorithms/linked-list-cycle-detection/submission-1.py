# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        seen = set()
        current = head
        seen.add(head)
        while current.next :
            if current.next in seen :
                return True
            current = current.next
            seen.add(current)
        return False