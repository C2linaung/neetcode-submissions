class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            jump_count = nums[i]
            for j in range(1, jump_count + 1):
                if i + j >= len(nums):
                    break
                dp[i + j] = min(dp[i + j], 1 + dp[i])
        return dp[-1]