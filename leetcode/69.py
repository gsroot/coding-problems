from math import floor


class Solution:
    def mySqrt(self, x: int) -> int:
        xn = x
        while abs(xn * xn - x) >= 1:
            xn = (xn + x / xn) / 2
        return floor(xn)


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(4))
    print(s.mySqrt(8))
