# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDist(node,son):
    if son is None :
        return 0
    else : 
        return max(maxDist(son,son.left),maxDist(son,son.right))+1

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        nodes = deque([root])
        diameter = 0
        while nodes :
            node = nodes.popleft()
            new = maxDist(node,node.left) + maxDist(node,node.right)
            if new > diameter :
                diameter = new
            if node.left is not None :
                nodes.append(node.left)
            if node.right is not None :
                nodes.append(node.right)
        return diameter
        
