# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None:
            return root is subRoot
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if self.isSameTree(node,subRoot) :
                return True
            if node.left is not None :
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is q
        if p.val != q.val :
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        