# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self,root,tree):
        if root.left:
            state,l,tree = self.inorder(root.left,tree)
            if state :
                return state,l,tree
        tree.append(root.val)
        if len(tree) == self.k:
            return True,len(tree),tree
        if root.right:
            state,l,tree = self.inorder(root.right,tree)
            if state :
                return state,l,tree
        return False, len(tree),tree

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        state, l, tree = self.inorder(root,[])
        return tree[k-1]