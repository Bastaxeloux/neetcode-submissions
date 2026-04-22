# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        to_inv = deque([root])
        treated_node, temp = TreeNode(), TreeNode()
        while to_inv:
            treated_node=to_inv[0]
            if treated_node.left : 
                to_inv.append(treated_node.left)
            if treated_node.right : 
                to_inv.append(treated_node.right)
            temp = treated_node.left
            treated_node.left = treated_node.right
            treated_node.right = temp
            to_inv.popleft()
        return root        