# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        mp = {None: 0} # node: height
        d = 0
        while stack:
            node = stack[-1]
            if node.left and node.left not in mp: # not yet visited
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                lh = mp[node.left]
                rh = mp[node.right]
                mp[node] = 1 + max(lh, rh)
                d = max(d, rh + lh)
        return d

