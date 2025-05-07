# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        # 닫는 괄호 → 여는 괄호 매핑
        pair = {")": "(", "]": "[", "}": "{"}
        stack = []

        for ch in s:
            # 여는 괄호면 스택에 추가
            if ch in pair.values():
                stack.append(ch)
            # 닫는 괄호면
            elif ch in pair:
                # 스택이 비어 있거나, 짝이 맞지 않으면 False
                if not stack or stack.pop() != pair[ch]:
                    return False
            else:
                # 허용되지 않는 문자
                return False

        # 남은 여는 괄호가 없으면 모두 짝이 맞는 것
        return not stack


if __name__ == "__main__":
    tests = ["()", "()[]{}", "(]", "([])"]
    for test in tests:
        result = Solution().isValid(test)
        print(result)
