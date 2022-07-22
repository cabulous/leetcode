from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        freq = sorted(list(count.values()), reverse=True)

        max_freq_allowed = len(s)
        res = 0

        for num in freq:
            if num > max_freq_allowed:
                res += num - max_freq_allowed
            max_freq_allowed = max(0, min(max_freq_allowed, num) - 1)

        return res
