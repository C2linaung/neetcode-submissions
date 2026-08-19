class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        best = 0
        while l < r:
            b = r - l
            if heights[l] < heights[r]:
                h = heights[l]
                l += 1
            else:
                h = heights[r]
                r -= 1
            best = max(best, h * b)
        return best