# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy1,dummy2 = ListNode(), ListNode()
        dummy1.next = l1
        dummy2.next = l2
        node1,node2 = dummy1, dummy2
        while node1.next and node2.next :
            temp = node1.next.val + node2.next.val
            if temp > 9:
                node1.next.val = temp%10
                if node1.next.next :
                    node1.next.next.val += 1
                else :
                    new = ListNode(1)
                    node1.next.next = new
            else :
                node1.next.val = temp
            node1 = node1.next
            node2 = node2.next
        if node2.next :
            node1.next = node2.next
        while node1.next and node1.next.val>9:
            node1.next.val = node1.next.val%10
            if node1.next.next :
                node1.next.next.val += 1
            else :
                new = ListNode(1)
                node1.next.next = new
            node1 = node1.next
        return l1

