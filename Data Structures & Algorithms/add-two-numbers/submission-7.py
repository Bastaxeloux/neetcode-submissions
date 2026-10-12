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
        dummy,return_node = ListNode(),ListNode()
        return_node = dummy
        node1,node2 = l1,l2
        carry = 0
        while node1 or node2 or carry:
            new = ListNode()
            temp = self.valNode(node1) + self.valNode(node2) + carry
            new.val = temp%10
            carry = temp//10
            return_node.next = new
            return_node = return_node.next
            if node1 :
                node1 = node1.next
            if node2:
                node2 = node2.next
        return dummy.next