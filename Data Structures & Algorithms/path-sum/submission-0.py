# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        q = deque([(0, root)])
        while q:
            level_count = len(q)
            for _ in range(level_count):
                total, node = q.popleft()
                total += node.val
                if not node.left and not node.right and total == targetSum:
                    return True
                if node.left: q.append((total, node.left))
                if node.right: q.append((total, node.right))
        return False