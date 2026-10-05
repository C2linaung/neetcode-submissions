class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = []
        counter = Counter(tasks)
        for task in counter.values():
            heapq.heappush(max_heap, -task)
        
        waitQ = deque()
        time = 0
        while max_heap or waitQ:
            time += 1
            if max_heap:
                task = heapq.heappop(max_heap)
                task += 1
                if task != 0:
                    waitQ.append((task, time + n))
            
            if waitQ and waitQ[0][1] == time:
                heapq.heappush(max_heap, waitQ.popleft()[0])
        return time