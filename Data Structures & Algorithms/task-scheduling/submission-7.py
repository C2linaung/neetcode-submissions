class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = []
        for cnt in task_counts.values():
            heapq.heappush(max_heap, -cnt)
        wait_queue = deque()
        time = 0
        while wait_queue or max_heap:
            time += 1
            if max_heap:
                task = heapq.heappop(max_heap)
                task += 1
                if task != 0:
                    wait_queue.append((task, time + n))
            
            if wait_queue and wait_queue[0][1] == time:
                heapq.heappush(max_heap, wait_queue.popleft()[0])
        return time