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
            s_parent = curr
            while s.left:
                s_parent = s
                s = s.left
            curr.val = s.val
            if s_parent.left == s: # this is needed
                s_parent.left = s.right
            else: # this case is when parent is the node to delete
                s_parent.right = s.right 
        return root
        