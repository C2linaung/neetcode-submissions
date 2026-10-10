class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(left, total, arr):
            if total == target:
                res.append(arr.copy())
                return 

            for i in range(left, len(nums)):
                if total + nums[i] > target:
                    return  
                arr.append(nums[i]) # choose
                dfs(i, total + nums[i], arr) # search
                arr.pop() # restore
        
        dfs(0, 0, [])
        return res