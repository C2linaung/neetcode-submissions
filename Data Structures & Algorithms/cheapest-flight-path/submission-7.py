class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = [float('inf')] * n
        price[src] = 0
        for stop in range(k + 1):
            tmpPrice = price.copy()
            for s, d, p in flights:
                if price[s] == float('inf'):
                    continue
                tmpPrice[d] = min(tmpPrice[d], price[s] + p)
            price = tmpPrice
        return price[dst] if price[dst] != float('inf') else -1