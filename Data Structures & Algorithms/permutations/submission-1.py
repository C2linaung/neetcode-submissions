class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # fill by swapping 
        def backtrack(i_to_fill):
            if i_to_fill == len(nums): # all positions filled
                res.append(nums[:])
                return 

            for i in range(i_to_fill, len(nums)):
                nums[i], nums[i_to_fill] = nums[i_to_fill], nums[i]
                backtrack(i_to_fill + 1)
                nums[i], nums[i_to_fill] = nums[i_to_fill], nums[i]
        backtrack(0)
        return res