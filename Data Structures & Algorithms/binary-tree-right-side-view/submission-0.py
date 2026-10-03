# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self,root,depth,out):
        if not root :
            return
        if len(out) == depth:
            out.append(root.val)
        self.dfs(root.right,depth+1,out)
        self.dfs(root.left,depth+1,out)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        self.dfs(root,0,out)
        return out