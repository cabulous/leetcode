from collections import Counter
from typing import List

MOD = 10 ** 9 + 7


# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/discuss/917779/JavaC%2B%2BPython-Space-O(N)
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(target)
        res = [1] + [0] * n

        for i in range(len(words[0])):
            count = Counter(w[i] for w in words)
            for j in range(n - 1, -1, -1):
                res[j + 1] += res[j] * count[target[j]] % MOD

        return res[n] % MOD
