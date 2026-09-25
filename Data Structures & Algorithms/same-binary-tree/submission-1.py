# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if p and not q or q and not p: return False

        p_stack = [p]
        q_stack = [q]
        while p_stack and q_stack:
            nodeP = p_stack.pop()
            nodeQ = q_stack.pop()
            if nodeP and not nodeQ or nodeQ and not nodeP: return False
            if not nodeP and not nodeQ: continue
            if nodeP.val != nodeQ.val: return False
            p_stack.append(nodeP.left)
            p_stack.append(nodeP.right)
            q_stack.append(nodeQ.left)
            q_stack.append(nodeQ.right)
        return p_stack == q_stack