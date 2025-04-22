# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1

        # 부호 처리
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        rev = 0

        # 숫자 뒤집기
        while x_abs:
            x_abs, pop = divmod(x_abs, 10)
            rev = rev * 10 + pop

        # 최종값 생성 및 32-bit 범위 검사
        result = sign * rev
        if result < INT_MIN or result > INT_MAX:
            return 0
        return result


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (1534236469, 0),
    ]
    for inp, exp in tests:
        out = sol.reverse(inp)
        print(f"{inp:>12} → {out:>12}  (expected {exp})", "✅" if out == exp else "❌")
