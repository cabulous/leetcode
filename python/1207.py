from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter()
        for num in arr:
            freq[num] += 1
        all_freq = freq.values()
        return len(all_freq) == len(set(all_freq))
