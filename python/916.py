from typing import List
from collections import Counter


# https://leetcode.com/problems/word-subsets/discuss/175854/JavaC%2B%2BPython-Straight-Forward
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = Counter()
        for w in words2:
            count |= Counter(w)

        return [w for w in words1 if not count - Counter(w)]


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = Counter()
        for w in words2:
            next_count = Counter(w)
            for i, ch in enumerate(next_count):
                count[ch] = max(count[ch], next_count[ch])

        return [w for w in words1 if not count - Counter(w)]
