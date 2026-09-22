class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        best = float('inf')
        win_sum = 0
        for r, num in enumerate(nums):
            win_sum += num
            while win_sum >= target:
                best = min(best, r - l + 1)
                win_sum -= nums[l]
                l += 1
        return best if best != float('inf') else 0