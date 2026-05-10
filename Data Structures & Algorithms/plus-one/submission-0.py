class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                carry = 0
                digits[i] += 1
                break
            digits[i] = 0
        if carry: digits.insert(0, 1)
        return digits