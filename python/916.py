from typing import List
from collections import Counter


# https://leetcode.com/problems/word-subsets/discuss/175854/JavaC%2B%2BPython-Straight-Forward
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        c = Counter()
        for b in B:
            c |= Counter(b)
        return [a for a in A if not c - Counter(a)]


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        b_max = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                b_max[i] = max(b_max[i], c)

        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), b_max)):
                ans.append(a)

        return ans
