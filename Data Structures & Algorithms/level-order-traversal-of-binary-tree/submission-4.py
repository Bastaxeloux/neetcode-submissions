# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self,root,depth,out):
        if root is None:
            return
        # print(f"Val={root.val} and depth={depth}")
        if len(out) == depth:
            out.append([])
        out[depth].append(root.val)
        self.dfs(root.left,depth+1,out)
        self.dfs(root.right,depth+1,out)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        self.dfs(root,0,out)
        return out