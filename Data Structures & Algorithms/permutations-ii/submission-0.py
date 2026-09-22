from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = Counter(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for num in count:
                if count[num] == 0:
                    continue

                # choose
                path.append(num)
                count[num] -= 1

                # explore
                backtrack(path)

                # undo
                path.pop()
                count[num] += 1

        backtrack([])
        return res