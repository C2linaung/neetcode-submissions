class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        best_profit = 0
        for price in prices:
            if price < lowest:
                lowest = price
            else:
                best_profit = max(best_profit, price - lowest)
        return best_profit