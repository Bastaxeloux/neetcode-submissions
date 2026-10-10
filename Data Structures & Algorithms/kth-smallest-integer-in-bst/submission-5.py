# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self,root,tree):
        if root.left:
            state = self.inorder(root.left,tree)
            if state :
                return True
        tree.append(root.val)
        if len(tree) == self.k:
            return True
        if root.right:
            state = self.inorder(root.right,tree)
            if state :
                return True
        return False

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k,tree = k,[]
        self.inorder(root,tree)
        return tree[k-1]