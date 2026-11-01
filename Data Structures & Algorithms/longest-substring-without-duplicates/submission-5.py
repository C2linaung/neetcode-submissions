class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        best = 0
        for r in range(len(s)):
            while s[r] in window:
                best = max(best, r - l)
                window.remove(s[l])
                l += 1
            window.add(s[r])
        return max(best, len(s) - l)
            