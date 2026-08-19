class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = dict() # (diff, index)
        for i, num in enumerate(nums):
            diff = target - num
            if diff in diffs:
                return [diffs[diff], i]
            diffs[num] = i
        return None