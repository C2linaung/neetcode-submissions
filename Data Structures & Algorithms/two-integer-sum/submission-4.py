class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = dict() # num: index
        for i, num in enumerate(nums):
            needed_diff = target - num
            if needed_diff in diffs.keys():
                return [diffs[needed_diff],i]
            diffs[num] = i
        return None