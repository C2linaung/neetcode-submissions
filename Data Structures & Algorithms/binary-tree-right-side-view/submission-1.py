# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        frontier = deque([root])
        res = []
        while frontier:
            level_count = len(frontier) - 1
            right_node = frontier.popleft()
            res.append(right_node.val)
            if right_node.right: frontier.append(right_node.right)
            if right_node.left: frontier.append(right_node.left)
            for _ in range(level_count):
                node = frontier.popleft()
                if node.right: frontier.append(node.right)
                if node.left:frontier.append(node.left)
        return res
