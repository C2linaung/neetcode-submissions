
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        best = 0

        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 0:
                    continue

                stack = [(x, y)]
                grid[y][x] = 0
                area = 0

                while stack:
                    x0, y0 = stack.pop()
                    area += 1

                    for dx, dy in directions:
                        nx, ny = x0 + dx, y0 + dy

                        if (0 <= nx < cols and
                            0 <= ny < rows and
                            grid[ny][nx] == 1):

                            grid[ny][nx] = 0
                            stack.append((nx, ny))

                best = max(best, area)

        return best
