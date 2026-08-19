class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = dict() # seen: index
        for i, num in enumerate(nums):
            diff_needed = target - num
            if diff_needed in seen_dict:
                return [seen_dict[diff_needed], i]
            seen_dict[num] = i
        return None