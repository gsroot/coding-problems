# https://leetcode.com/problems/group-anagrams/description/
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s)

        return list(anagrams.values())


if __name__ == '__main__':
    result = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result)
