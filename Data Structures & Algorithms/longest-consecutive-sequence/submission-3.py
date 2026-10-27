class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h_map = defaultdict(int)
        res = 0
        for num in nums:
            if not h_map[num]:
                h_map[num] = 1 + h_map[num - 1] + h_map[num + 1]
                h_map[num - h_map[num - 1]] = h_map[num]
                h_map[num + h_map[num + 1]] = h_map[num]
                res = max(res, h_map[num])
        return res