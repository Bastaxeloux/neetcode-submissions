# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDist(root,son):
    if son is None :
        return 0
    else : 
        return 1 + max(maxDist(son,son.left),maxDist(son,son.right))


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue1 = deque([root])
        diam = 0
        while queue1 :
            temp = 0
            root1 = queue1.popleft()
            if root1.left is not None:
                queue1.append(root1.left)
            if root1.right is not None:
                queue1.append(root1.right)
            temp = maxDist(root1,root1.left) + maxDist(root1,root1.right)
            if temp > diam :
                diam = temp
        return diam
            
                

