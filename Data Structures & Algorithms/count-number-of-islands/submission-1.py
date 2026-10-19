class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1,0), (0, -1), (-1, 0), (0, 1)]
        stack = []
        res = 0
        for r in range(m):
            for c in range(n):
                is_island = False
                if grid[r][c] == "1": 
                    stack.append((c, r))
                    is_island = True
                while stack:
                    x, y = stack.pop()
                    grid[y][x] = "0" # visited
                    for dx, dy in directions:
                        x_next, y_next = x + dx, y + dy
                        if (
                            0 <= x_next < n 
                            and 0 <= y_next < m
                            and grid[y_next][x_next] == "1"
                        ):
                            stack.append((x_next, y_next))
                if is_island: res += 1
        return res
                