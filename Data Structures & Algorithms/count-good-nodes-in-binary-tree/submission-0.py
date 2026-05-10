# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def preOrder(node, best):
            nonlocal count
            if not node:
                return
            
            if (node.val >= best):
                count += 1
            best = max(best, node.val)
            preOrder(node.left, best)
            preOrder(node.right, best)
            pass
        preOrder(root, -float("inf"))
        return count