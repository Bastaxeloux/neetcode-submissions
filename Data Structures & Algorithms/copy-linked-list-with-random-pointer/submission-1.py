"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node = head
        new_head = new = Node(0)
        corres = dict()
        while node :
            new.val = node.val
            if node.next :
                temp = Node(0)
                new.next = temp
            else :
                new.next = None
            temp2 = node.next
            corres[node] = new
            node = temp2
            new = new.next
        node = head
        p2 = new_head
        while node :
            if node.random:
                p2.random = corres[node.random]
            else :
                p2.random = None
            node = node.next
            p2 = p2.next
        return new_head