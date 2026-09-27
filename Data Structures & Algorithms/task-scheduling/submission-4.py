class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = []
        for count in task_counts.values():
            heapq.heappush(max_heap, -count)
        
        t = 0
        q = deque() # store of (task_count, time_ready)
        while q or max_heap:
            t += 1
            if max_heap:
                task = heapq.heappop(max_heap)
                task += 1 # since task is in negative
                if task != 0: q.append((task, t + n))
            
            if q and q[0][1] == t:
                heapq.heappush(max_heap, q.popleft()[0])
        return t
                