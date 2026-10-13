class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        out = []
        def search(start_i, total, arr):
            if total == target:
                out.append(arr.copy())
                return
            
            for i in range(start_i, len(nums)):
                if total + nums[i] > target:
                    return 
                arr.append(nums[i]) # choose
                search(i, total + nums[i], arr) # search
                arr.pop() # restore
        
        search(0, 0, [])
        return out