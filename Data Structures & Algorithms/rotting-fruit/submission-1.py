class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((c, r))
        
        time = 0
        while q:
            level_length = len(q)
            for _ in range(level_length):
                x, y = q.popleft()
                for dx, dy in directions:
                    x_new, y_new = x + dx, y + dy
                    if (
                        0 <= x_new < len(grid[0]) and
                        0 <= y_new < len(grid) and 
                        grid[y_new][x_new] == 1
                    ):
                        q.append((x_new, y_new))
                        grid[y_new][x_new] = 2
            if q: time += 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return time
                        
