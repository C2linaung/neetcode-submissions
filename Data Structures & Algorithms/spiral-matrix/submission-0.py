class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        dir_order = 0
        directions = [(1,0), (0, -1), (-1, 0), (0, 1)]
        m, n = len(matrix), len(matrix[0])
        x, y = 0, 0
        while len(res) != (m * n):
            res.append(matrix[y][x])
            matrix[y][x] = 101 # mark visited
            for _ in range(4):
                dx, dy = directions[dir_order]
                x_next, y_next = x + dx, y + dy
                if (
                    0 <= x_next < n 
                    and 0 <= y_next < m
                    and matrix[y_next][x_next] != 101
                ):
                    x, y = x_next, y_next
                    break
                else:
                    dir_order += 1
                    dir_order %= 4
        return res
