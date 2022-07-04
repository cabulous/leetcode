class Solution:
    def minDeletions(self, s: str) -> int:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        freq.sort(reverse=True)

        max_freq_allowed = len(s)
        res = 0

        for num in freq:
            if num > max_freq_allowed:
                res += num - max_freq_allowed
            max_freq_allowed = max(0, min(max_freq_allowed, num) - 1)

        return res
