# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        parent = {root: None}
        while stack:
            node = stack.pop()
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if p in parent and q in parent:
                break
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            ancestors.add(q)
            q = parent[q]

        return q                