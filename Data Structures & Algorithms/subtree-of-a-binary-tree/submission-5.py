# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isEqual(root,subroot):
    if not root and not subroot:
        return True
    if not root and subroot:
        return False
    if root and not subroot:
        return False
    elif root.val == subroot.val :
        return isEqual(root.left,subroot.left) and isEqual(root.right,subroot.right)
    return False


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if root is None:
            return root is subroot
        return isEqual(root,subroot) or self.isSubtree(root.right,subroot) or self.isSubtree(root.left,subroot)