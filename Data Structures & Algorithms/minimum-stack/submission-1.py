class MinStack:

    def __init__(self):
        self.stack = []
        self.min_heap = [float('inf')]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.min_heap, min(val, self.min_heap[0]))
        

    def pop(self) -> None:
        self.stack.pop()
        heapq.heappop(self.min_heap)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_heap[0]
