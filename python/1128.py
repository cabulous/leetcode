from collections import Counter
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = Counter(tuple(sorted(x)) for x in dominoes)
        return sum([v * (v - 1) // 2 for v in count.values()])
