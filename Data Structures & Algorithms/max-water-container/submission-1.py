class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        best = 0
        while l < r:
            smaller = min(heights[l], heights[r])
            amount =  smaller * (r - l)
            best = max(amount, best)
            if heights[l] == smaller:
                l += 1
            else:
                r -= 1
        return best
