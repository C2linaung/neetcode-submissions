class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n_new = 0
            n_old = n
            while n_old != 0:
                n_new += ((n_old % 10) ** 2)
                n_old //= 10
            n = n_new
        return True