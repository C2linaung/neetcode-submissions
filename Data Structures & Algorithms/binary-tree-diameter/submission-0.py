# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0
        def height(node):
            nonlocal best
            if not node: return 0
            lh = height(node.left)
            rh = height(node.right)
            best = max(best, lh + rh)
            return max(lh, rh) + 1
        height(root)
        return best