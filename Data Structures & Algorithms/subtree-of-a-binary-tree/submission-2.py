# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isEqual(root, subroot):
    if root is None and subroot is None:
        return True
    if root is None or subroot is None:
        return False
    if root.val != subroot.val:
        return False
    return isEqual(root.left, subroot.left) and isEqual(root.right,subroot.right)

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if isEqual(root, subroot):
            return True
        if root is None:
            return False
        if self.isSubtree(root.left, subroot):
            return True
        if self.isSubtree(root.right, subroot):
            return True
        return False
       
