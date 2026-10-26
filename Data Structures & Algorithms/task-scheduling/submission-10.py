class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks)
        max_heap = []
        for cnt in task_counter.values():
            heapq.heappush(max_heap, -cnt)
        
        time = 0
        q = deque()
        while max_heap or q:
            time += 1
            if max_heap:
                task = heapq.heappop(max_heap)
                task += 1
                if task != 0:
                    q.append((task, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time