# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        def inOrder(node):
            nonlocal k, res
            if not node:
                return
            
            inOrder(node.left)
            if k == 1: res = node.val
            k -= 1
            inOrder(node.right)
        inOrder(root)
        return res