class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = [0]
        for i in range(1,n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                top_index = stack.pop(-1)
                ans[top_index] = i - top_index
            stack.append(i)
        return ans