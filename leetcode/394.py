# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        cnt_stack, str_stack = [], []
        num, curr_str = 0, ""
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                cnt_stack.append(num)
                str_stack.append(curr_str)
                num, curr_str = 0, ""
            elif c == "]":
                cnt = cnt_stack.pop()
                prev = str_stack.pop()
                curr_str = prev + curr_str * cnt
            else:
                curr_str += c
        return curr_str