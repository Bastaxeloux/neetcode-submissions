# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self,root):
        if root.left:
            self.inorder(root.left)
        self.tree.append(root.val)
        if root.right:
            self.inorder(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.tree = []
        self.inorder(root)
        return self.tree[k-1]