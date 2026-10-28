class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for w in stones:
            heapq.heappush(max_heap, -w)
        while len(max_heap) > 1:
            s1 = heapq.heappop(max_heap)
            s2 = heapq.heappop(max_heap)
            if s1 == s2: continue
            heapq.heappush(max_heap, s1 - s2)
        
        return -max_heap[0] if max_heap else 0