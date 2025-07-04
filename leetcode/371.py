# https://leetcode.com/problems/sum-of-two-integers
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while (b & mask) > 0:
            c = (a & b) << 1
            a = (a ^ b)
            b = c

        return (a & mask) if b > 0 else a
