class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        best = 0
        for p in prices:
            smallest = min(smallest, p)
            best = max(best, p - smallest)
        return best