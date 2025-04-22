# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 1) 음수는 모두 false
        # 2) 10으로 나누어 떨어지면서 0이 아닌 수는 뒤집었을 때 앞자리가 0이 되므로 false
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_half = 0
        # x가 뒤집은 값보다 커지는 동안만 반복
        while x > reverted_half:
            # 뒤에서 한 자리씩 꺼내서 reverted_half에 붙이기
            reverted_half = reverted_half * 10 + (x % 10)
            x //= 10

        # 길이가 짝수인 경우: x == reverted_half
        # 길이가 홀수인 경우: 가운데 숫자가 reverted_half에 한 번 더 붙어 있으므로 //10
        return x == reverted_half or x == reverted_half // 10


if __name__ == "__main__":
    sol = Solution()
    test_cases = [121, -121, 10, 123123, 21120]
    for tc in test_cases:
        print(f"Input: {tc:>4} → Output: {sol.isPalindrome(tc)}")
