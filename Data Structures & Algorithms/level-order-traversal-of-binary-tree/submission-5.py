# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root,0)])
        out = []
        if root is None :
            return out
        while queue :
            node,depth = queue.popleft()
            if node.left :
                queue.append((node.left,depth+1))
            if node.right :
                queue.append((node.right,depth+1))
            if len(out) == depth :
                out.append([node.val])
            else :
                out[depth].append(node.val)
        return out