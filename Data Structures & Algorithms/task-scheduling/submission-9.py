class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = []
        task_counter = Counter(tasks)
        for count in task_counter.values():
            heapq.heappush(max_heap, -count)
        q = deque() # wait queue (task_count, ttr)
        time = 0
        while max_heap or q: # still have tasks to process
            time += 1
            if max_heap:
                task_count = heapq.heappop(max_heap)
                task_count += 1
                if task_count != 0:
                    q.append((task_count, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time