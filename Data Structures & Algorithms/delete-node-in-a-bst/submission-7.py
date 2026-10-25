# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        parent = None
        curr = root
        while curr and curr.val != key:
            parent = curr
            if curr.val < key:
                curr = curr.right
            else:
                curr = curr.left
        if not curr: return root # no key found
        if not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right
            if not parent: return child
            if curr == parent.left:
                parent.left = child
            else:
                parent.right = child
        else: # 2 child
            s, s_parent = curr.right, curr
            while s.left:
                s_parent = s
                s = s.left
            curr.val = s.val
            if s == s_parent.left:
                s_parent.left = s.right
            else:
                s_parent.right = s.right

        return root