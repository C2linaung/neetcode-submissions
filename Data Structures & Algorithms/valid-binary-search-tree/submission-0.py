# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def inOrder(node):
            nonlocal arr
            if not node:
                return
            inOrder(node.left)
            arr.append(node.val)
            inOrder(node.right)
        
        def isIncreasing(arr):
            arr_len = len(arr)
            if arr_len <= 1:
                return True

            prev = arr[0]
            for i in range(1, arr_len):
                curr = arr[i]
                if curr <= prev:
                    return False
                prev = curr
            return True

        inOrder(root)   
        return isIncreasing(arr)