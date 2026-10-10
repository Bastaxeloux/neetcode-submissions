# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidLR(self,root):
        if root is None :
            return True, float('inf'), float("-inf")
        stateL, ltree_min, ltree_max = self.isValidLR(root.left)
        stateR, rtree_min, rtree_max = self.isValidLR(root.right)
        if not (stateL and stateR) :
            return False,0,0
        if not ltree_max < root.val < rtree_min :
            return False,0,0
        return True, min(root.val,ltree_min,rtree_min),max(root.val,ltree_max,rtree_max)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        state,lmin,rmin = self.isValidLR(root)
        return state
        
        
        
        