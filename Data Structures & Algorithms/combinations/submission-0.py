class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            
            for i in range(start, n + 1):
                path.append(i) # add i (take)
                backtrack(i + 1, path)
                path.pop()     # remove i (no take)
        backtrack(1, [])
        return res