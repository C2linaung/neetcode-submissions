# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        frontier_p = [p]
        frontier_q = [q]
        while frontier_p and frontier_q:
            p_node = frontier_p.pop()
            q_node = frontier_q.pop()
            if p_node == None and q_node == None:
                continue

            if not p_node or not q_node or p_node.val != q_node.val:
                return False
            frontier_p.append(p_node.left)
            frontier_q.append(q_node.left)
            frontier_p.append(p_node.right)
            frontier_q.append(q_node.right)
        return True