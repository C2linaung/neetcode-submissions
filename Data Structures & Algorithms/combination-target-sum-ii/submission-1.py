class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        candidates.sort()
        def search(arr, i, total):
            if total == target:
                out.append(arr.copy())
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]: continue 
                if total + candidates[j] > target: break
                arr.append(candidates[j])
                search(arr, j + 1, total + candidates[j])
                arr.pop()
        
        search([], 0, 0)
        return out