# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]


if __name__ == '__main__':
    s = input()
    result = Solution().isPalindrome(s)
    print(result)
