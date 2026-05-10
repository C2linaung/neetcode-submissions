class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        saved_end = -float('inf')
        for start, end in intervals:
            if start >= saved_end: # no collision
                saved_end = end
                continue
            
            # Collision
            if end < saved_end: # with smaller end
                saved_end = end
            
            count += 1
        return count