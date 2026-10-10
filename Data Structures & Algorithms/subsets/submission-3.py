class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            tmp = []
            for subset in output:
                tmp.append(subset + [num])
            output += tmp

        return output
