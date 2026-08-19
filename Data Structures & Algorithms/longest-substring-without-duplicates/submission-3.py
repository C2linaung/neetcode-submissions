class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        window = set()
        best = 0
        while r < len(s):
            if s[r] in window:
                best = max(best, r - l)
                window.remove(s[l])
                l += 1
                continue
            window.add(s[r])
            r += 1
        return max(best, r - l)