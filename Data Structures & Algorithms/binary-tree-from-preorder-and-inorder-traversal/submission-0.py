# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        in_idx = 0  # pointer in inorder

        for val in preorder[1:]:
            node = TreeNode(val)

            # If the top of stack hasn't matched inorder[in_idx] yet,
            # the next preorder node must be in the left subtree.
            if stack[-1].val != inorder[in_idx]:
                stack[-1].left = node
                stack.append(node)
            else:
                # Pop nodes whose inorder position is complete,
                # then attach the new node as the right child.
                last = None
                while stack and stack[-1].val == inorder[in_idx]:
                    last = stack.pop()
                    in_idx += 1
                last.right = node
                stack.append(node)

        return root