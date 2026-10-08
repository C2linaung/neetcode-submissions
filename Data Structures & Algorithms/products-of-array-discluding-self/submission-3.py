class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        for i in range(1, len(nums)):
            res.append(res[-1] * nums[i - 1])
        
        acc = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= acc
            acc *= nums[i]
        return res