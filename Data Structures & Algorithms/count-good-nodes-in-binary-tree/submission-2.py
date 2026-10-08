# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def dfs(self,node,maxval):
        if node is None:
            return
        if not maxval > node.val:
            self.count += 1
        self.dfs(node.left,max(maxval,node.val))
        self.dfs(node.right,max(maxval,node.val))
    
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root,root.val-1)
        return self.count