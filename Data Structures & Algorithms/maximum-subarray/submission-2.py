class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
            # idea is at every number, decide either to add
            # to the previous sum or to restart
        return max(dp)