from typing import List
from collections import Counter


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter = Counter()
        for word in words2:
            word_counter = Counter(word)
            for ch, count in word_counter.items():
                counter[ch] = max(counter[ch], count)

        return [w for w in words1 if not counter - Counter(w)]


# https://leetcode.com/problems/word-subsets/discuss/175854/JavaC%2B%2BPython-Straight-Forward
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter = Counter()
        for word in words2:
            counter |= Counter(word)

        return [w for w in words1 if not counter - Counter(w)]
