# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        print(f"root={root.val},p={p.val} and q={q.val}")
        if min(p.val,q.val) <= root.val <= max(p.val,q.val) :
            print("found")
            return root
        elif p.val < root.val :
            print("going left")
            return self.lowestCommonAncestor(root.left,p,q)
        else : 
            print("going right")
            return self.lowestCommonAncestor(root.right,p,q)