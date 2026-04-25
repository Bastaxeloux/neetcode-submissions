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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None :
            return True
        queue = deque([root])
        balanced = True
        while queue:
            dist_left, dist_right = 0,0
            print("queue=",queue)
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
                dist_left = maxDist(node,node.left)
            if node.right is not None:
                queue.append(node.right)
                dist_right = maxDist(node,node.right)
            dif = abs(dist_right-dist_left)
            if dif > 1 :
                balanced = False
        return balanced
