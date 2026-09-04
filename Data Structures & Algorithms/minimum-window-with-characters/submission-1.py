class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        l = r = 0
        have, need = 0, len(countT)
        saved, savedLen = (0, 0), float("inf")
        while r < len(s):
            if s[r] in countT:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] == countT[s[r]]: have += 1

            while have == need:
                if r - l < savedLen:
                    saved = (l, r)
                    savedLen = r - l + 1
                
                if s[l] in countT:
                    if window[s[l]] == countT[s[l]]:
                        have -= 1
                    window[s[l]] -= 1
                l += 1
            r += 1
        return s[saved[0]: saved[1] + 1] if savedLen != float("infinity") else ""
