class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i_to_swap):
            if i_to_swap == len(nums):
                res.append(nums[:])
                return 

            for i in range(i_to_swap, len(nums)):
                nums[i], nums[i_to_swap] = nums[i_to_swap], nums[i]
                backtrack(i_to_swap + 1)
                nums[i], nums[i_to_swap] = nums[i_to_swap], nums[i]
        backtrack(0)
        return res