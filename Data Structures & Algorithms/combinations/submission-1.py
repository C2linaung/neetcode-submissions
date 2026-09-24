class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        def backtrack(i, path):
            if len(path) == k:
                output.append(path.copy())
            
            for j in range(i, n + 1):
                path.append(j)
                backtrack(j + 1, path)
                path.pop()
        
        backtrack(1, [])
        return output