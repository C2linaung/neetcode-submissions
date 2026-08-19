class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        min_heap = []
        for key, v in counter.items():
            if len(min_heap) == k:
                heapq.heappush(min_heap, (v, key))
                heapq.heappop(min_heap)
            else:
                heapq.heappush(min_heap, (v, key))
        return [key for _, key in min_heap]