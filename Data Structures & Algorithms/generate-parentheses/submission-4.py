class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = [("", 0, 0)]

        while stack:
            s, open_count, close_count = stack.pop()

            if open_count == n and close_count == n:
                res.append(s)
                continue

            if open_count < n:
                stack.append((s + "(", open_count + 1, close_count))

            if close_count < open_count:
                stack.append((s + ")", open_count, close_count + 1))

        return res