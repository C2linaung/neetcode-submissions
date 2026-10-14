# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        curr = root
        parent = None
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if not curr: return root # no key found
        
        if not curr.left or not curr.right:
            if not parent: return root.right if root.right else root.left
            child = curr.left if curr.left else curr.right
            if curr == parent.left:
                parent.left = child
            else:
                parent.right = child
        else:
            s_parent = curr
            s = curr.right
            while s.left:
                s_parent = s
                s = s.left
            curr.val = s.val
            if s == s_parent.left:
                s_parent.left = s.right
            else:
                s_parent.right = s.right              
        return root