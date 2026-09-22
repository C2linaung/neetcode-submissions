class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def sumRange(self, left: int, right: int) -> int:
        total = 0
        for i in range(left, right + 1):
            total += self.arr[i]
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)