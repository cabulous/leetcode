from typing import List
from collections import defaultdict


# https://leetcode.com/problems/number-of-matching-subsequences/discuss/117634/Efficient-and-simple-go-through-words-in-parallel-with-explanation
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        for word in words:
            waiting[word[0]].append(iter(word[1:]))

        for ch in s:
            for suffix in waiting.pop(ch, ()):
                next_ch = next(suffix, None)
                waiting[next_ch].append(suffix)

        return len(waiting[None])
