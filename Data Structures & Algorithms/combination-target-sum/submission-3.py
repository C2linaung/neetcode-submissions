class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(total, i, arr):
            nonlocal res
            if total == target:
                res.append(arr.copy())
                return
            for j in range(i, len(nums)):
                if total + nums[j] > target: return
                arr.append(nums[j]) # choose
                dfs(total + nums[j], j, arr)
                arr.pop()
        
        dfs(0, 0, [])
        return res