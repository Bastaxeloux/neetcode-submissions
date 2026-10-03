# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self,root):
        if not root :
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        totaldepth = self.maxDepth(root)
        out = []
        for _ in range(totaldepth):
            out.append([])
        if root is None :
            return []
        queue = deque([(root,0)])
        while queue :
            #print(queue)
            node,depth = queue.popleft()
            if node.left : 
                queue.append((node.left,depth+1))
            if node.right : 
                queue.append((node.right,depth+1))
            out[depth].append(node.val)
        return out
        


        