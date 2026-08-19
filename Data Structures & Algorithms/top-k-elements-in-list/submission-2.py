class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = Counter(nums)
        min_heap = [(0, 0) for _ in range(k)] # (val, key)
        for k, v in num_counter.items():
            if v > min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (v, k))
        return [k for v, k in min_heap]