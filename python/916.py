from typing import List
from collections import Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter = Counter()
        for word in words2:
            next_counter = Counter(word)
            for ch, count in next_counter.items():
                counter[ch] = max(counter[ch], count)

        return [w for w in words1 if not counter - Counter(w)]


# https://leetcode.com/problems/word-subsets/discuss/175854/JavaC%2B%2BPython-Straight-Forward
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = Counter()
        for w in words2:
            count |= Counter(w)

        return [w for w in words1 if not count - Counter(w)]
