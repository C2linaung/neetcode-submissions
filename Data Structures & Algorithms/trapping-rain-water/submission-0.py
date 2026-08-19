class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left, max_right = height[l], height[r]
        trapped = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                max_left = max(max_left, height[l])
                trapped += (max_left - height[l]) 
            else:
                r -= 1
                max_right = max(max_right, height[r])
                trapped += (max_right - height[r])
        return trapped