# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBal = True
        def h(node):
            nonlocal isBal
            if not node: return 0
            lh, rh = h(node.left), h(node.right)
            if abs(lh - rh) > 1: isBal = False
            return max(lh, rh) + 1
        h(root)
        return isBal
        
