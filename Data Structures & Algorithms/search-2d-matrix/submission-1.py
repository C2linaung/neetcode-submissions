class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        # search through rows
        l, r = 0, m
        while l < r:
            mid = (l + r) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] <= target:
                l = mid + 1
            else:
                r = mid
        # search through col
        col = l - 1
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[col][mid] == target:
                return True
            elif matrix[col][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False