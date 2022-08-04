from typing import List
from collections import Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = Counter()
        for word in words2:
            curr_count = Counter(word)
            for ch, ch_count in curr_count.items():
                count[ch] = max(count[ch], ch_count)

        return [w for w in words1 if not count - Counter(w)]


# https://leetcode.com/problems/word-subsets/discuss/175854/JavaC%2B%2BPython-Straight-Forward
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = Counter()
        for word in words2:
            count |= Counter(word)

        return [w for w in words1 if not count - Counter(w)]
