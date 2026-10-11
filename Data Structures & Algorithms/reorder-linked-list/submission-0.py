# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        start, startp1 = head, head.next
        while startp1 :
            print(f"start={start.val} et startp1 = {startp1.val}")
            endm1, end = start,startp1
            while end.next :
                endm1,end = end, end.next
            print(f"end-1={endm1.val} et end = {end.val}")
            endm1.next = None
            start.next = end
            if end != startp1:
                end.next = startp1
            start, startp1 = startp1, startp1.next
