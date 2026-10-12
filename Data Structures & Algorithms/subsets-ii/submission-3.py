class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = [[]]
        last = idx = 0
        for i, num in enumerate(nums):
            tmp = []
            idx = last if i >= 1 and nums[i] == nums[i - 1] else 0
            last = len(output)
            for j in range(idx, last):
                tmp.append(output[j] + [num])
            output += tmp
        return output