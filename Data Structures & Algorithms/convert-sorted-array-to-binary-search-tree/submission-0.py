class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = len(nums) // 2
        q = deque()
        root = TreeNode(nums[mid])
        q.append((root, 0, mid - 1))
        q.append((root, mid + 1, len(nums) - 1))
        while q:
            p, l, r = q.popleft()
            if l <= r:
                mid = (l + r) // 2
                child = TreeNode(nums[mid])
                if child.val < p.val:
                    p.left = child
                else:
                    p.right = child
                q.append((child, l, mid - 1))
                q.append((child, mid + 1, r))
        return root