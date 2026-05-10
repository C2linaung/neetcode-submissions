class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = dict() # diff : index
        for i, num in enumerate(nums):
            if num in diff_dict.keys():
                return [diff_dict[num], i]
            diff_needed = target - num
            diff_dict[diff_needed] = i
        return None
