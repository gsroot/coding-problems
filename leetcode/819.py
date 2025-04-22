# https://leetcode.com/problems/most-common-word/
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        import re
        from collections import Counter
        words = [word for word in re.findall(r'\w+', paragraph.lower()) if word not in banned]
        counter = Counter(words)
        return counter.most_common(1)[0][0]


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    result = Solution().mostCommonWord(paragraph, banned)
    print(result)