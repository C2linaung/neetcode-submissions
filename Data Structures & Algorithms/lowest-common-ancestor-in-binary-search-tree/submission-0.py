# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        small = 0
        big = 0
        if p.val < q.val:
            small, big = p.val, q.val
        else:
            big, small = p.val, q.val
        curr = root
        while True:
            if curr.val > big:
                curr = curr.left
            elif curr.val < small:
                curr = curr.right
            else:
                return curr