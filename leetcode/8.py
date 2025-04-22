# https://leetcode.com/problems/string-to-integer-atoi
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1

        i, n = 0, len(s)
        # 1. skip leading whitespace
        while i < n and s[i] == " ":
            i += 1

        # 2. sign
        sign = 1
        if i < n and s[i] in ("+", "-"):
            if s[i] == "-":
                sign = -1
            i += 1

        # 3. read digits
        start = i
        while i < n and s[i].isdigit():
            i += 1
        digit_str = s[start:i]
        if not digit_str:
            return 0

        # 4. convert and clamp
        num = sign * int(digit_str)
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("42", 42),
        ("   -042", -42),
        ("1337c0d3", 1337),
        ("0-1", 0),
        ("words and 987", 0),
        ("2147483648", 2**31 - 1),  # 경계 테스트: overflow
        ("-2147483649", -(2**31)),  # 경계 테스트: underflow
        ("", 0),  # 빈 문자열
        ("   +0 123", 0),  # 0 읽고 중단
        ("  +00123", 123),  # leading zero 처리
    ]

    for s, expected in tests:
        result = sol.myAtoi(s)
        print(f"Input: {s!r:>15} → Output: {result:>11} (Expected: {expected})")
