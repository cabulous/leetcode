from typing import List
from collections import defaultdict


# https://leetcode.com/problems/number-of-matching-subsequences/discuss/117634/Efficient-and-simple-go-through-words-in-parallel-with-explanation
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)

        for w in words:
            waiting[w[0]].append(iter(w[1:]))

        for c in s:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)

        return len(waiting[None])
