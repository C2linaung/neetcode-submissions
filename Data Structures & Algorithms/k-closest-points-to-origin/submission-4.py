class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for (x, y) in points:
            dist = - (x*x + y*y)
            if len(max_heap) == k:
                if dist > max_heap[0][0]:
                    heapq.heappush(max_heap, (dist, [x, y]))
                    heapq.heappop(max_heap)
            else:
                heapq.heappush(max_heap, (dist, [x, y]))
        return [p for _, p in max_heap]
            