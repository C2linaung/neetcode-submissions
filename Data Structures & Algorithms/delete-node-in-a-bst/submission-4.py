# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root
        parent = None
        curr = root
        while curr:
            if key < curr.val:
                parent = curr
                curr = curr.left
            elif key > curr.val:
                parent = curr
                curr = curr.right
            else:
                break
        if not curr: return root # no key
        if not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right
            if not parent: return child # root node removal
            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child
        else:
            s = curr.right
            s_parent = curr
            while s.left:
                s_parent = s
                s = s.left
            curr.val = s.val
            if s_parent.left == s:
                s_parent.left = s.right
            else:
                s_parent.right = s.right
        return root