# https://leetcode.com/problems/reverse-string/
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


if __name__ == '__main__':
    s = [x for x in input()]
    Solution().reverseString(s)
    print(s)
