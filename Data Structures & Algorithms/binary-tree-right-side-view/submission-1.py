# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        if root is None :
            return out
        queue = deque([(root,0)])
        while queue :
            #print(queue)
            node,depth = queue.popleft()
            if node.right : 
                queue.append((node.right,depth+1))
            if node.left : 
                queue.append((node.left,depth+1))
            if len(out) == depth:
                out.append(node.val)
        return out