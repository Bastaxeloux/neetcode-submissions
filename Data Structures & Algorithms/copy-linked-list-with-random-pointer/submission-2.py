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
        node = head
        corres = dict()
        corres[None] = None
        while node :
            new = Node(node.val)
            corres[node] = new
            node = node.next
        node = head
        while node :
            corres[node].next = corres[node.next]
            corres[node].random = corres[node.random]
            node = node.next
        return corres[head]