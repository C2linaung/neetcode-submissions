class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = 0
        def findPath(r, c):
            nonlocal count
            if r == m or c == n: 
                return
            if r == m - 1 and c == n - 1:
                count += 1
            
            findPath(r + 1, c)
            findPath(r, c + 1)

        findPath(0, 0)
        return count