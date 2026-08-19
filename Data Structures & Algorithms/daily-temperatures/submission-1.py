class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            if not stack or temp < stack[-1][1]:
                stack.append((i, temp))
                continue
            
            # stack exists and temp > stack top
            while stack and temp > stack[-1][1]:
                top, _ = stack.pop()
                res[top] = i - top
            
            stack.append((i, temp))
        return res