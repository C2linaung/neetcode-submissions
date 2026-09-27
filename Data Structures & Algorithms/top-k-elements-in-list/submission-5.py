class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        for num, cnt in counts.items():
            freq[cnt].append(num)
        res = []
        for i in range(len(freq) - 1, 0 , -1):
            for nums in freq[i]:
                res.append(nums)
                if len(res) == k:
                    return res