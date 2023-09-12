from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        all_freq = sorted(list(count.values()), reverse=True)
        max_freq = len(s)
        res = 0

        for freq in all_freq:
            if freq > max_freq:
                res += freq - max_freq
            max_freq = max(0, min(max_freq, freq) - 1)

        return res
