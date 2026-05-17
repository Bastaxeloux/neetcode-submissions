# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isIn(root,p):
    if root is None :
        return False
    nodes = deque([root])
    while nodes:
        node = nodes.popleft()
        if node.val == p.val :
            return True
        if node.left is not None:
            nodes.append(node.left)
        if node.right is not None:
            nodes.append(node.right)
    return False

def path(root,p):
    path_of_p = [root]
    if isIn(root.left,p):
        path_of_p.extend(path(root.left,p))
        return path_of_p
    if isIn(root.right,p):
        path_of_p.extend(path(root.right,p))
        return path_of_p
    return path_of_p

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_p = path(root,p)
        path_p.reverse()
        path_q = path(root,q)
        path_q.reverse()
        print(f"Path_p = {path_p} and Path_q = {path_q}")
        for node in path_p :
            if node in path_q:
                return node
