class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = [intervals[0]]
        if len(intervals) == 1:
            return stack
        for start, end in intervals[1:]:
            if start <= stack[-1][1] < end:
                stack[-1][1] = end
            elif start > stack[-1][1]:
                stack.append([start, end])
        return stack
