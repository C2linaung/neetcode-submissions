# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root
        curr = root
        parent = None
        while curr:
            if key < curr.val:
                parent = curr
                curr = curr.left
            elif key > curr.val:
                parent = curr
                curr = curr.right
            else:
                break
        if not curr: return root # no key found

        if not curr.left or not curr.right: # 0 or 1 child
            child = curr.left if curr.left else curr.right
            if not parent : return child # if node to remove is the root
            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child
        else: # 2 child
            s = curr.right
            s_parent = None
            while s.left:
                s_parent = s
                s = s.left
            if s_parent:
                s_parent.left = s.right
                s.right = curr.right
            s.left = curr.left
            if not parent: return s # s is new root is root is removed
            if parent.left == curr:
                parent.left = s
            else:
                parent.right = s
        return root
        