# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def valNode(self,node):
        if node is None:
            return 0
        else :
            return node.val

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        node1,node2,carry = l1,l2,0
        while node1 or node2 or carry:
            temp = self.valNode(node1) + self.valNode(node2) + carry
            new = ListNode(temp%10) 
            carry = temp//10
            tail.next = new
            tail = tail.next
            if node1 :
                node1 = node1.next
            if node2:
                node2 = node2.next
        return dummy.next