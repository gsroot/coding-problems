# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_pos = {}        # 문자 → 가장 최근 인덱스
        left = 0             # 현재 윈도우의 왼쪽 경계
        max_len = 0

        for right, ch in enumerate(s):
            # 이미 본 문자라면, 중복이 발생하지 않도록 윈도우 왼쪽 경계를 이동
            if ch in last_pos and last_pos[ch] >= left:
                left = last_pos[ch] + 1
            # 현재 문자의 위치 갱신
            last_pos[ch] = right
            # 윈도우 길이 계산 및 최댓값 갱신
            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == '__main__':
    tests = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "dvdf"
    ]
    for test in tests:
        result = Solution().lengthOfLongestSubstring(test)
        print(result)