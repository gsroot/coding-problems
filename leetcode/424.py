class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        left = 0
        max_freq = 0
        best = 0

        for right, c in enumerate(s):
            idx = ord(c) - 65
            freq[idx] += 1
            max_freq = max(max_freq, freq[idx])

            wsize = right - left + 1
            while wsize - max_freq > k:
                freq[ord(s[left]) - 65] -= 1
                left += 1
                wsize -= 1

            best = max(best, wsize)

        return best