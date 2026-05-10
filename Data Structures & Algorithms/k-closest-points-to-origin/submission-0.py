class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i in range(k):
            p = points[i]
            heapq.heappush(max_heap, (-math.hypot(p[0], p[1]), p))
        
        for i in range(k, len(points)):
            p = points[i]
            heapq.heappush(max_heap, (-math.hypot(p[0], p[1]), p))
            heapq.heappop(max_heap)
        
        return [p for _, p in max_heap]
