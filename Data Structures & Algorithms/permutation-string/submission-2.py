class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        s1_counter = [0] * 26
        w = [0] * 26
        w_len = 0
        w_size = len(s1)
        for c in s1:
            s1_counter[ord(c) - ord('a')] += 1
        
        for r, c in enumerate(s2):
            if w_len < w_size:
                w[ord(c) - ord('a')] += 1
                w_len += 1
                continue
            
            if w == s1_counter:
                return True
            
            w[ord(s2[r - w_size]) - ord('a')] -= 1
            w[ord(c) - ord('a')] += 1
        
        return w == s1_counter