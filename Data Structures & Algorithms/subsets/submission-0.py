class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for x in nums:
            res += [curr + [x] for curr in res]
        return res