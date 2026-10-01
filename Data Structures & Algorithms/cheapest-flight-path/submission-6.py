class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = [float('inf')] * n
        price[src] = 0
        for i in range(k + 1):
            tmpPrices = price.copy()
            for s, d, p in flights:
                if price[s] == float('inf'):
                    continue
                tmpPrices[d] = min(tmpPrices[d], price[s] + p)
            price = tmpPrices
        return price[dst] if price[dst] != float('inf') else -1