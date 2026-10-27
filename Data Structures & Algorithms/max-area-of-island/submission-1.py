class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        best = 0
        seen = set()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                seen.add((x, y))
                if grid[y][x] == 0:
                    continue
                stack = [(x, y)]
                area = 0
                while stack:
                    area += 1
                    x_0, y_0 = stack.pop()
                    seen.add((x_0, y_0))
                    for dx, dy in directions:
                        x_n, y_n = x_0 + dx, y_0 + dy
                        if (
                            0 <= x_n < len(grid[0]) and
                            0 <= y_n < len(grid) and
                            grid[y_n][x_n] == 1 and  
                            (x_n, y_n) not in seen
                        ):
                            stack.append((x_n, y_n))
                            seen.add((x_n, y_n))
                best = max(area, best)
        return best
