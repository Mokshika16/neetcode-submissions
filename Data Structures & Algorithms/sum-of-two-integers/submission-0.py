class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        # Convert unsigned to signed
        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)

        return a