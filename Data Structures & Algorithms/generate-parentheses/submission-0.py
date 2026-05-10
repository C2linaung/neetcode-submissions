class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(s, open_count, close_count):
            nonlocal res
            if open_count == n and close_count == n:
                res.append(s)
            
            if open_count < n:
                generate(s + "(", open_count + 1, close_count)
            
            if close_count < open_count:
                generate(s + ")", open_count, close_count + 1)
        generate("", 0, 0)
        return res