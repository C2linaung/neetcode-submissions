class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = []
        for freq in task_counts.values():
            heapq.heappush(max_heap, -freq)
        waitQ = deque() # (task_cnt_left, time_ready)
        t = 0
        while max_heap or waitQ:
            t += 1
            if max_heap:
                task = heapq.heappop(max_heap)
                task += 1
                if task != 0:
                    waitQ.append((task, t + n))
            
            if waitQ and waitQ[0][1] == t:
                heapq.heappush(max_heap, waitQ.popleft()[0])
        return t